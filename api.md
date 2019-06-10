### 提示

    账号请联系管理员在/admin/ 界面生成

    创建容器耗时较长
    请使用 获取容器详情的接口轮询 (一般15s内完成)
    可以通过

### 认证

#### 获取 token

    url
        POST '/api-token-auth/'
    body json
        {
          "username": "username",
          "password": "password"
        }

    result:
        {
            "token": "f13d790f573badf63ad9c108841546eb73caf68f"
        }

### 获取数据

#### 获取 容器列表

    url GET '/app/'

    headers
        Authorization: Token f13d790f573badf63ad9c108841546eb73caf68f

    result:
        [
            {
                "kind": 1,
                "conf_text": "{}",
                "create_time": "2019-06-02 07:59",
                "pub_time": "2019-06-02 07:59",
                "port": "",
                "container_id": "",
                "uuid": "fb12031f-b902-4159-a939-550d910535f4"
            },
            {
                "kind": 1,
                "conf_text": "{\"mem_limit\": 1024}",
                "create_time": "2019-06-02 07:45",
                "pub_time": "2019-06-02 07:45",
                "port": "{\"6379/tcp\": [{\"HostIp\": \"0.0.0.0\", \"HostPort\": \"32770\"}]}",
                "container_id": "9b219d34e30f104481367bd7428093be268f4ef536ec4ca23a62df38d4de7443",
                "uuid": "8d237c58-ed1f-4f1c-b408-e8cdfbf133d7"
            },
            {
                "kind": 0,
                "conf_text": "{\"MYSQL_ROOT_PASSWORD\": \"CME0GPEN\", \"MYSQL_DATABASE\": \"8Y8MF0\", \"MYSQL_USER\": \"JK4R3J\", \"MYSQL_PASSWORD\": \"O106M16P\", \"character-set-server\": \"utf8mb4\", \"collation-server\": \"utf8mb4_unicode_ci\"}",
                "create_time": "2019-06-02 07:43",
                "pub_time": "2019-06-02 07:43",
                "port": "{\"3306/tcp\": [{\"HostIp\": \"0.0.0.0\", \"HostPort\": \"32769\"}], \"33060/tcp\": [{\"HostIp\": \"0.0.0.0\", \"HostPort\": \"32768\"}]}",
                "container_id": "c9cd48b03b78153a8a6b45a5fe4f43828b6b3f2dd916406962a08e874462bad8",
                "uuid": "249be0a9-dfb7-4c00-8725-5fcf694a0d39"
            }
        ]

#### 创建容器
    url
        POST '/app/'
    headers
        Authorization: Token f13d790f573badf63ad9c108841546eb73caf68f
    body[json]
        {
            "kind": 0, //0 为mysql, 1 为redis
            "conf_text": "{}" //{\"character-set-server\": \"utf8mb4\", \"collation-server\": \"utf8mb4_unicode_ci\"} mysql 可选
            // {\"mem_limit\": 1024} redis 可选 单位mb
        }
    result: [code:201]
        {
            "kind": 0,
            "conf_text": "{}",
            "create_time": "2019-06-02 10:24",
            "pub_time": "2019-06-02 10:24",
            "port": "",
            "container_id": "",
            "uuid": "d9e0192e-5f00-4bcf-bdfd-971c02261117"
        }

#### 获取 容器详情
    url
        GET '/app/249be0a9-dfb7-4c00-8725-5fcf694a0d39/'

    headers
        Authorization: Token f13d790f573badf63ad9c108841546eb73caf68f

    result: [code:200]
        {
            "kind": 0,
            "conf_text": "{\"MYSQL_ROOT_PASSWORD\": \"CME0GPEN\", \"MYSQL_DATABASE\": \"8Y8MF0\", \"MYSQL_USER\": \"JK4R3J\", \"MYSQL_PASSWORD\": \"O106M16P\", \"character-set-server\": \"utf8mb4\", \"collation-server\": \"utf8mb4_unicode_ci\"}",
            "create_time": "2019-06-02 07:43",
            "pub_time": "2019-06-02 07:43",
            "port": "{\"3306/tcp\": [{\"HostIp\": \"0.0.0.0\", \"HostPort\": \"32769\"}], \"33060/tcp\": [{\"HostIp\": \"0.0.0.0\", \"HostPort\": \"32768\"}]}",
            "container_id": "c9cd48b03b78153a8a6b45a5fe4f43828b6b3f2dd916406962a08e874462bad8",
            "uuid": "249be0a9-dfb7-4c00-8725-5fcf694a0d39"
        }


#### 删除 容器
    url
        DELETE '/app/249be0a9-dfb7-4c00-8725-5fcf694a0d39/'

    headers
        Authorization: Token f13d790f573badf63ad9c108841546eb73caf68f

    result: [code:204]
