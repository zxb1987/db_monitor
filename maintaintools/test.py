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
                    print('主机 {0} 目录 {1} 存在，正在上传{2}文件！'.format(queryset.host, upload_path, files.name))
                    sftp.put(file_path, upload_dir)
                    print('文件 {0} 上传成功！'.format(files.name))
                    try:
                        print('开始保存数据。。。。。。。。。。。。')
                        upload_record = UploadDownFileInfo.objects.create(file_name=files.name, file_path=upload_dir,
                                                                          file_size=file_size, file_host=queryset.host,
                                                                          file_type=1)

                        upload_record.save()
                        print('保存数据：{0} 完成！！'.format(upload_record))
                    except Exception as e:
                        print('记录保存失败：%s' % e)
                    sftp.close()
                except Exception as e:
                    print('主机 {0} 路径不存在：{1}'.format(queryset.host, e))
                    sftp.mkdir(upload_path)
                    print('创建目录 {0} 成功'.format(upload_path))
                    sftp.chdir('%s' % upload_path)
                    sftp.put(file_path, upload_dir)
                    print('文件:{0} 上传成功!'.format(files.name))
                    try:
                        print('开始保存数据。。。。。。。。。。。。')
                        upload_record = UploadDownFileInfo.objects.create(file_name=files.name, file_path=file_path,
                                                                          file_size=file_size, file_host=queryset.host,
                                                                          file_type=1)
                        print('正在保存数据：{0}'.format(upload_record))

                        upload_record.save()
                    except Exception as e:
                        print('记录保存失败：%s' % e)
                    sftp.close()

                t.close()
                # return HttpResponse('上传成功')

            return HttpResponse('999999999999999999999999999')
        except Exception as e:
            print('22222222222222222')
            return HttpResponse({"code": 400, "msg": u"上传失败%s" % e})
