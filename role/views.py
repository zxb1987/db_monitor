import logging

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters

from role.serializers import *
from role.serializers import RoleListSerializer


# Create your views here.
class ApiRoLelist(generics.ListCreateAPIView):
    queryset = RoleList.objects.get_queryset().order_by('id')
    serializer_class = RoleListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'role_name',)
    search_fields = ('id', 'role_name', 'role_code', 'role_status', 'role_remark', 'role_add_date', 'role_update_date',)
    ordering_fields = ('role_name', 'role_code', 'role_status', 'role_remark', 'role_add_date', 'role_update_date',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = RoleList.objects.get_queryset().order_by('id')
    queryset = RoleList.objects.get_queryset().order_by('role_code')
    serializer_class = RoleListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
