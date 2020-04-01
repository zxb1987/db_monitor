from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions

from role.serializers import *
from role.serializers import RoleListSerializer


# Create your views here.
class ApiRolelist(generics.ListCreateAPIView):
    def get_queryset(self):
        print("----------------views>ApiRolelist-----------------------")
        id = self.request.query_params.get('id', None)
        role_name = self.request.query_params.get('role_name', None)
        role_code = self.request.query_params.get('role_code', None)
        return RoleList.objects.filter(id=id, role_name=role_name, role_code=role_code).order_by('id')

    serializer_class = RoleListSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = RoleList.objects.get_queryset().order_by('role_code')
    #print(queryset)
    serializer_class = RoleListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
