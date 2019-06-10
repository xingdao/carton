# _*_ coding:utf-8 _*_

import logging
import uuid

from rest_framework import generics

from api.models import App
from api.serializers import AppSerializer
from api.tasks import add, remove
from carton import my_permissions

logger = logging.getLogger(__name__)


class AppList(generics.ListCreateAPIView):
    """
    """
    permission_classes = (my_permissions.IsOwner,)
    serializer_class = AppSerializer

    def get_queryset(self):
        return App.objects.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        app = serializer.save(user=self.request.user,
                              uuid=str(uuid.uuid4()))
        add.delay(app.uuid)


class AppDetail(generics.RetrieveDestroyAPIView):
    """
    """
    permission_classes = (my_permissions.IsOwner,)
    queryset = App.objects.all()
    serializer_class = AppSerializer

    lookup_field = 'uuid'

    def perform_destroy(self, instance):
        remove.delay(instance.uuid)
        # instance.delete()

