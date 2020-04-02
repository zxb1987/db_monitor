import logging

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters

from role.serializers import *
from role.serializers import RoleListSerializer


# Create your views here.
class ApiRolelist(generics.ListCreateAPIView):
    # def get_queryset(self):
    #     print("----------------views>ApiRolelist-----------------------")
    # #     print(1)
    #     # id = self.request.query_params.get('id', None)
    #     role_name = self.request.query_params.get('role_name', None)
    #     role_code = self.request.query_params.get('role_code', None)
    #     return RoleList.objects.filter(role_name=role_name, role_code=role_code).order_by('role_code')
    # serializer_class = RoleListSerializer
    # filter_backends = (DjangoFilterBackend,)
    # permission_classes = (permissions.DjangoModelPermissions,)
    logger = logging.getLogger(__name__)
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    queryset = RoleList.objects.get_queryset().order_by('id')
    serializer_class = RoleListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'role_name',)
    search_fields = ('id', 'role_code',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = RoleList.objects.get_queryset().order_by('id')
    serializer_class = RoleListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
