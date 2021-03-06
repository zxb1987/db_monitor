"""
@Time ： 2020/05/15 12:04
@Auth ： sq
@File ：test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os

import paramiko
from django.http import HttpResponse
from django.views import View

from assets.models import LinuxList
from maintaintools.models import UploadDownFileInfo


#  计算文件大小的函数
def covertFileSizes(size):
    kb = 1024
    mb = kb * 1024
    gb = mb * 1024
    tb = gb * 1024

    if size >= tb:
        return "%.1f TB" % float(size / tb)
    if size >= gb:
        return "%.1f GB" % float(size / gb)
    if size >= mb:
        return "%.1f MB" % float(size / mb)
    if size >= kb:
        return "%.1f KB" % float(size / kb)


class FileUpload(View):
    '''
    上传文件接口
    '''

    def post(self, request):
        try:
            data = request.POST.get('data')  # 携带参数
            files = request.FILES.get('file')  # 文件
            file_size = covertFileSizes(files.size)
            print('获得文件: {0} 文件大小:{1}'.format(files, file_size))
            save_path = os.path.join(os.path.abspath("../db_monitor"))  # 获取文件夹相对路径
            file_path = save_path + r'\upload_file\%s' % files  # 相对路径拼接文件
            upload_path = r'/home/lecentfile/'
            upload_dir = r'/home/lecentfile/%s' % files.name  # 服务器接收文件路径
            if files is None:
                return HttpResponse("没有需要上传的文件")
            else:
                # 打开特定的文件进行二进制的写操作
                with open(file_path, 'wb+') as f:
                    # 分块写入文件
                    print('文件正在保存到：%s' % file_path)
                    for chunk in files.chunks():
                        f.write(chunk)
                # return HttpResponse("上传完成!")
            print(file_path, '123\n123', upload_dir)
            for hostid in data.split(','):
                queryset = LinuxList.objects.get(id=hostid)
                print(' 得主机IP：%s：' % queryset.host)
                t = paramiko.Transport((queryset.host, queryset.sshport))
                t.connect(username=queryset.user, password=queryset.password)
                sftp = paramiko.SFTPClient.from_transport(t)
                print('连接成功')
                try:
                    # sftp.stat(upload_dir)#判断文件夹是否存在，不存在就创建
                    sftp.chdir('%s' % upload_path)  # 判断文件夹是否存在，不存在就创建
                    print('主机 {0} 目录 {1} 存在，正在上传{2}文件！'.format(queryset.host, upload_dir, files.name))
                    sftp.put(file_path, upload_dir)
                    print('文件 {0} 上传成功！'.format(files.name))
                    sftp.close()
                except Exception as e:
                    print('主机 {0} 路径不存在：{1}'.format(queryset.host, e))
                    sftp.mkdir(upload_path)
                    print('创建目录 {0} 成功'.format(upload_path))
                    sftp.chdir('%s' % upload_path)
                    print('主机 {0} 目录 {1} 存在，正在上传{2}文件！'.format(queryset.host, upload_dir, files.name))
                    sftp.put(file_path, upload_dir)
                    print('文件:{0} 上传成功!'.format(files.name))
                    sftp.close()
                t.close()
                try:
                    print('开始保存数据。。。。。。。。。。。。')
                    upload_record = UploadDownFileInfo.objects.create(file_name=files.name, file_path=upload_dir,
                                                                      file_size=file_size, file_host=queryset.host,
                                                                      file_type=1)
                    print('正在保存数据：{0}'.format(upload_record))
                    upload_record.save()
                except Exception as e:
                    print('记录保存失败：%s' % e)
                # return HttpResponse('上传成功')
            return HttpResponse('999999999999999999999999999')
        except Exception as e:
            print('22222222222222222')
            return HttpResponse({"code": 400, "msg": u"上传失败%s" % e})

    # class GetFolder(View):
    def get(self, request,ssh_id):
        queryset = LinuxList.objects.get(id=ssh_id)
        val = request.body
        print(ssh_id)
        print(queryset)
        reult_folder=''
        # get_sshfolder='find / -path /proc -prune -o -type d -user root -print'
        get_sshfolder = 'cd /home && ls -1'
        # 实例化SSHClient
        client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # 连接SSH服务端，以用户名和密码进行认证
            client.connect(hostname=queryset.host, port=queryset.sshport, username=queryset.user, password=queryset.password)
            # 打开一个Channel并执行命令
            # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值，get_pty=True 从服务器请求一个伪终端(默认' ' False ' ')。见“.Channel.get_pty”
            stdin, stdout, stderr = client.exec_command(get_sshfolder, get_pty=True)
            # 打印执行结果
            res, err = stdout.read().decode('utf-8'), stderr.read().decode('utf-8')  # 第二方案
            fval=[]
            reult_folder = res if res else err
            fval.append(reult_folder)
            # print('11111111')
            # print(fval)
            a=1
            for fileall in fval:

                print(fileall)
                # if fileall.startswith('d'):
                #     print('当前是文件夹')
                # else:
                #     print('当前是文件')

            # 关闭SSHClient
            client.close()
        except Exception as e:
            print('服务器 {0} 连接失败！请检查登录的用户名密码是否正确！！'.format(queryset.hostname))
            print(e)
        # dfs_showdir(reult_folder,0)
        return HttpResponse(reult_folder)
        # val = json.loads(request.body)
    # print(val)

