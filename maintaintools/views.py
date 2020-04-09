from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from role.serializers import *
from maintaintools.serializers import MaintainToolsSerializer
from maintaintools.models import MaintainCommand


# Create your views here.
class ApiMaintainCommandList (generics.ListCreateAPIView):
    queryset = MaintainCommand.objects.get_queryset().order_by('id')
    serializer_class = MaintainToolsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id',)
    search_fields = ('id', 'commname', 'command', 'commandparam')
    ordering_fields = ('id', 'commname', 'command', 'commandparam')
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiMaintainCommandDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = MaintainCommand.objects.get_queryset().order_by('id')
    # queryset = RoleList.objects.get_queryset().order_by('role_code')
    serializer_class = MaintainToolsSerializer
    permission_classes = (permissions.DjangoModelPermissions,)

