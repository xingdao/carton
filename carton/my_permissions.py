# _*_ coding:utf-8 _*_

"""
@author: qiao
"""

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated():
            return obj.user == request.user
        return False
