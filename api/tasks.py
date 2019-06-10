# _*_ coding:utf-8 _*_
import json
import logging
import os
import random
import string
import time
import redis
import docker
import MySQLdb
from celery import shared_task
from docker.errors import NotFound

from api.models import App, AppType

logger = logging.getLogger(__name__)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def run_mysql(app):
    """
    environment={'MYSQL_ROOT_PASSWORD': 'my-secret-pw', 'MYSQL_DATABASE': 'db_name', 'MYSQL_USER': 'user',
                 'MYSQL_PASSWORD': 'password'},
    command='--character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci'
    """
    environment = {'MYSQL_ROOT_PASSWORD': id_generator(8), 'MYSQL_DATABASE': id_generator(6),
                   'MYSQL_USER': id_generator(6), 'MYSQL_PASSWORD': id_generator(8)}
    command = {'character-set-server': 'utf8mb4', 'collation-server': 'utf8mb4_unicode_ci'}

    conf = json.loads(app.conf_text)
    for x in conf.keys():
        # 暂时不开放自定义
        # if x in ['MYSQL_ROOT_PASSWORD', 'MYSQL_DATABASE', 'MYSQL_USER', 'MYSQL_PASSWORD']:
        #     environment.update({x: conf[x]})
        if x in ['character-set-server', 'collation-server']:
            command.update({x: conf[x]})

    client = docker.from_env()
    container = client.containers.run(
        detach=True,
        name=app.uuid,
        image='mysql:latest',
        # 目前自动分配
        # ports={3060: 8080},
        publish_all_ports=True,
        # 保存数据到对应的文件
        volumes=['home/ubuntu/data/{}:/var/lib/mysql'.format(app.uuid)],
        environment=dict(**environment, **{'MYSQL_ROOT_HOST': '%'}),
        command=' '.join(['--{0}={1}'.format(x, command[x]) for x in command.keys()])
    )
    start = int(time.time())

    while (int(time.time()) - start) < 15:
        container.reload()
        # 检查 服务是否启动
        if container.ports:
            try:
                MySQLdb.connect(host='127.0.0.1', user=environment['MYSQL_USER'], passwd=environment['MYSQL_PASSWORD'],
                                db=environment['MYSQL_DATABASE'], charset=environment['character-set-server'],
                                port=int(container.ports['3060/tcp'][0]['HostPort']), connect_timeout=1).cursor().execute('SHOW DATABASES')
                break
            except Exception as e:
                logger.info('uuid:[{0}] waiting start ports:[{1}] error:[{2}]'.format(app.uuid, container.ports, e), exc_info=True)
        time.sleep(1)
    container.reload()
    app.container_id = str(container.id)
    app.port = json.dumps(container.ports)
    app.logs = str(container.logs())[-1500:]
    app.conf_text = json.dumps(dict(**environment, **command))
    app.save()


def run_redis(app):
    """
    """
    mem_limit = 1024
    conf = json.loads(app.conf_text)
    if str(conf.get('mem_limit')).isdigit() and int(conf['mem_limit']) < 1024:
        mem_limit = int(conf['mem_limit'])

    command = {'requirepass': id_generator(8)}
    client = docker.from_env()
    container = client.containers.run(
        detach=True,
        name=app.uuid,
        image='redis:latest',
        mem_limit='{}m'.format(mem_limit),
        # 目前自动分配
        # ports={6379: 6379},
        publish_all_ports=True,
        # 保存数据到对应的文件
        volumes=['/home/ubuntu/data/{}:/data'.format(app.uuid)],
        command=' '.join(['--{0} {1}'.format(x, command[x]) for x in command.keys()])
    )
    start = int(time.time())

    while (int(time.time()) - start) < 15:
        container.reload()
        # 检查 服务是否启动
        if container.ports and container.ports.get('6079/tcp') and isinstance(container.ports.get('6079/tcp'), list):
            try:
                conn = redis.StrictRedis(host='localhost',
                                         password=command['requirepass'],
                                         port=int(container.ports['6079/tcp'][0]['HostPort']))
                conn.ping()
                break
            except Exception as e:
                logger.info('uuid:[{0}] waiting start ports:[{1}] error:[{2}]'.format(app.uuid, container.ports, e),
                            exc_info=True)
        time.sleep(1)

    container.reload()
    app.container_id = str(container.id)
    app.port = json.dumps(container.ports)
    app.logs = str(container.logs())[-1500:]
    app.conf_text = json.dumps(dict(**{'mem_limit': mem_limit}, **command))
    app.save()


@shared_task
def add(uuid):
    try:
        app = App.objects.get(uuid=uuid)

        path = '/home/ubuntu/data/{}'.format(app.uuid)
        if not os.path.exists(path):
            os.makedirs(path)

        if app.kind == AppType.MySQL:
            run_mysql(app)
        elif app.kind == AppType.Redis:
            run_redis(app)
        else:
            raise ValueError('kind:[{}]'.format(app.kind))
    except Exception as e:
        logger.error('add uuid:[{0}] error:[{1}]'.format(e, uuid), exc_info=True)
        raise e


@shared_task
def remove(uuid):
    # stop container
    # remove container
    # remove data ??
    # remove app
    try:
        app = App.objects.get(uuid=uuid)
        client = docker.from_env()
        container = client.containers.get(app.container_id)
        container.reload()
        container.stop()
        container.remove()
        app.delete()
    except NotFound:
        App.objects.filter(uuid=uuid).delete()
        logger.warning('remove uuid:[{0}] warning containers NotFound'.format(uuid))
    except Exception as e:
        logger.error('remove uuid:[{0}] error:[{1}]'.format(e, uuid), exc_info=True)
        raise e
