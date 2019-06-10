# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

import json
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AppType:
    MySQL = 0
    Redis = 1


APP_TYPE_KIND_CHOICES = ((AppType.MySQL, 'MySQL'),
                         (AppType.Redis, 'Redis'))


def validate_json(value):
    try:
        json.loads(value)
    except Exception as e:
        raise ValidationError('%(value)s error[info]',
                              params={'value': value, 'error': str(e)})


class App(models.Model):
    class Meta:
        verbose_name = '容器属性'
        verbose_name_plural = '容器属性'

    def __unicode__(self):
        return '{0}[1]'.format(self.kind, self.uuid)

    user = models.ForeignKey(User, verbose_name='用户', editable=False)
    kind = models.IntegerField(verbose_name='类型', choices=APP_TYPE_KIND_CHOICES)
    port = models.CharField(verbose_name='端口', max_length=200, editable=False)
    uuid = models.CharField(verbose_name='uuid', max_length=128, editable=False)
    container_id = models.CharField(verbose_name='容器ID', max_length=128, editable=False)
    conf_text = models.TextField(verbose_name='配置内容', max_length=400, validators=[validate_json])
    logs = models.TextField(verbose_name='容器日志', max_length=1500, editable=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, editable=False)
    pub_time = models.DateTimeField(verbose_name='修改时间', auto_now=True, editable=False)


class ApiLog(models.Model):
    class Meta:
        verbose_name = '请求日志'
        verbose_name_plural = '请求日志'

    def __unicode__(self):
        return '{0}[1]'.format(self.behavior, self.uuid)

    uuid = models.CharField(verbose_name='uuid', max_length=40)
    behavior = models.CharField(verbose_name='行为', max_length=40)
    result = models.TextField(verbose_name='结果', max_length=400)
    conf_text = models.TextField(verbose_name='配置内容', max_length=400)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_created=True)
