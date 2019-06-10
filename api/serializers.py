# _*_ coding:utf-8 _*_

"""
@author: qiao
"""
from rest_framework import serializers

from api.models import App


class AppSerializer(serializers.ModelSerializer):
    """
    """

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M", label='创建时间', read_only=True)
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M", label='修改时间', read_only=True)
    port = serializers.CharField(label='端口', read_only=True)
    container_id = serializers.CharField(label='容器ID', read_only=True)
    uuid = serializers.CharField(label='uuid', read_only=True)

    class Meta:
        model = App
        fields = ('kind', 'conf_text', 'create_time', 'pub_time', 'port', 'container_id', 'uuid')
