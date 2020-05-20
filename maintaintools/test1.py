"""
@Time ： 2020/04/24 10:14
@Auth ： 孙权
@File ：test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os

import paramiko

upload_dir = '/home/lecentfile'
t = paramiko.Transport(('192.168.1.25', 22))
t.connect(username='root', password='lecent123')
sftp = paramiko.SFTPClient.from_transport(t)

is_exists = os.path.exists(upload_dir)
print('连接成功')
# if not os.path.exists(upload_dir):
#     print('目录不存在')
#     sftp.mkdir(upload_dir)
#     print('创建目录成功')
#     print(upload_dir)
# else:
#     print(upload_dir)

if is_exists is False:
    sftp.mkdir(upload_dir)
    print('{0} 创建成功'.format(upload_dir))
else:
    print('{0} 目录已存在.'.format(upload_dir))
