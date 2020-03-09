# encoding:utf-8

from .models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *

# Ecs Api           drf 中文文档   http://drf.jiuyou.info/#/drf/requests
class ApiUserList(generics.ListCreateAPIView):
    queryset = UserList.objects.get_queryset().order_by('id')
    serializer_class = UserListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host','linux_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限

class ApiUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserList.objects.get_queryset().order_by('id')
    serializer_class = UserListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
