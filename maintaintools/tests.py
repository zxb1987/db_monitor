import paramiko
from django.http import HttpResponse
import requests
import json

# from utils import tools
# import paramiko
#
# date = tools.now()
# print(
#     date
# )

def hello(requests,args=None):
    val=json.loads(requests.body)
    print(val)



    return HttpResponse('123456')


#
# # 实例化SSHClient
# client = paramiko.SSHClient()
#
# # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # 连接SSH服务端，以用户名和密码进行认证
# client.connect(hostname='192.168.1.25', port=22, username='root', password='lecent123')
#
# # 打开一个Channel并执行命令
# stdin, stdout, stderr = client.exec_command('cat /home/config.log')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
#
# # 打印执行结果
# print(stdout.read().decode('utf-8'))
# print(stderr.read().decode('utf-8'))
#
# # 关闭SSHClient
# client.close()
#
# class SSHClient(requests):
#     print(requests)
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


# if __name__ == '__main__':
#     params = {
#         'hostname': '192.168.1.25',
#         'port': 22,
#         'username': 'root',
#         'password': 'lecent123'
#     }
#     linux_conn, _ = SSHClient(params).connection()
