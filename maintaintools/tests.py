import paramiko
from django.views import View
from django.http import HttpResponse
import json
from maintaintools.models import MaintainCommand


class getpaerm(View):
    def post(self, request, r_id):
        print(r_id)
        queryset = MaintainCommand.objects.get(id=r_id)
        ssh_cmd = queryset.usecommand + ' ' + queryset.commandparam
        print(ssh_cmd)
        val = json.loads(request.body)
        allval = []
        host = ''
        sshport = 22
        user = ''
        password = ''
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
        text_commd = stdout.read().decode('utf-8'), stderr.read().decode('utf-8')
        # 关闭SSHClient
        client.close()

        return HttpResponse(text_commd)
