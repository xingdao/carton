# _*_ coding:utf-8 _*_
from __future__ import unicode_literals


class AppType:
    MySQL = 0
    Redis = 1


APP_TYPE_KIND_CHOICES = ((AppType.MySQL, 'MySQL'),
                         (AppType.Redis, 'Redis'))

