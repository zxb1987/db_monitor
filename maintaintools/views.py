import paramiko
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from maintaintools.serializers import *
from maintaintools.models import MaintainCommand


# Create your views here.
class ApiMaintainCommandList(generics.ListCreateAPIView):
    queryset = MaintainCommand.objects.get_queryset().order_by('id')
    serializer_class = MaintainToolsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id',)
    search_fields = ('id', 'commname', 'usecommand', 'commandparam')
    ordering_fields = ('id', 'commname', 'usecommand', 'commandparam')
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限


class ApiMaintainCommandDetail(generics.RetrieveUpdateDestroyAPIView):
    print("----------------views>ApiRoleDetail-----------------------")
    queryset = MaintainCommand.objects.get_queryset().order_by('id')
    serializer_class = MaintainToolsSerializer
    permission_classes = (permissions.DjangoModelPermissions,)

#
# class ApiSSHClient(generics.ListCreateAPIView):
#     def __init__(self, params):
#         self.params = params
#         self.hostname = self.params['hostname']
#         self.port = self.params['port']
#         self.username = self.params['username']
#         self.password = self.params['password']
#
#     def connection(self):
#         self.params = self.convert_params(self.params)
#         ssh_client = paramiko.SSHClient()
#         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#         try:
#             ssh_client.connect(**self.params)
#             print("ssh_client")
#             print(ssh_client)
#             t = paramiko.Transport((self.hostname, self.port))
#             t.connect(username=self.username, password=self.password)
#             sftp_client = paramiko.SFTPClient.from_transport(t)
#             print("sftp_client")
#             print(sftp_client)
#             return ssh_client, sftp_client
#         except Exception as e:
#             print("linux 链接错误")
#             print(e)
#             return (None, None)
#
#     def ssh_exec_command(self):
#         command = 'find -name'
#         res = super().exec_command(command, self.conn)
#         res = res.readlines()
#         app_url = {}
#         for line in res:
#             if line.startswith('tomcat'):
#                 app_url = line.split()[1]
#
#         return {
#             'app_url': app_url
#         }
