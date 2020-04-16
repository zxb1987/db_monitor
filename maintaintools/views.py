import json
import paramiko
from django.views import View
from django.http import HttpResponse
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


class GetPaerm(View):
    def post(self, request, ssh_id):
        queryset = MaintainCommand.objects.get(id=ssh_id)
        ssh_cmd = queryset.usecommand + ' ' + queryset.commandparam
        val = json.loads(request.body)
        allval = []
        text_commd = ''
        for i in val:
            allval.append(i)
        for val in allval:
            host = val.get('host')
            sshport = val.get('sshport')
            user = val.get('user')
            password = val.get('password')
            # 实例化SSHClient
            client = paramiko.SSHClient()
            # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接SSH服务端，以用户名和密码进行认证
            client.connect(hostname=host, port=sshport, username=user, password=password)
            # 打开一个Channel并执行命令
            stdin, stdout, stderr = client.exec_command(ssh_cmd)  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
            # 打印执行结果
            text_commd = str(text_commd + '\n' + stdout.read().decode('utf-8'))
            # 关闭SSHClient
            client.close()
        return HttpResponse(text_commd)
