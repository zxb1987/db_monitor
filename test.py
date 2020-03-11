#基于ssh,用于连接远程服务器做操作：远程执行命令，上传或下载文件
import paramiko
passworda='JX123qwe'
#创建一个ssh对象
client = paramiko.SSHClient()
#2.解决问题：首次连接，会出现
# Are you sure you want to continue connecting (yes/no)? yes
# 自动选择yes

# 允许连接不在know_hosts文件中的主机
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#3.连接服务器
client.connect(hostname='119.3.4.222',port=22,username='root',password=passworda)

#4.执行操作
stdin,stdout,stderr = client.exec_command('hostname')#标准输入，标准输出，标准错误输出。
#Execute a command on the SSH server.  A new `.Channel` is opened and
# the requested command is executed.  The command's input and output
# streams are returned as Python ``file``-like objects representing
# stdin, stdout, and stderr.

#5.获取命令的执行结果
res = stdout.read().decode('utf-8')#使结果具有可读性

print(res)

#6.断开连接
client.close()
#6.断开连接
client.close()
#6.断开连接
client.close()