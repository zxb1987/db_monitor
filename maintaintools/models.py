from django.db import models
from django.utils import timezone


class MaintainCommand(models.Model):
    commname = models.CharField('命令名称', max_length=200)
    usecommand = models.CharField('执行命令', max_length=200, blank=True, null=True)
    commandparam = models.CharField('命令参数', max_length=200, blank=True)
    createtime = models.DateTimeField("创建时间", default=timezone.now, blank=True, null=True)
    updatedtime = models.DateTimeField("更新时间", default=timezone.now, blank=True, null=True)
    remark = models.CharField('备注', max_length=200, blank=True)

    def __str__(self):
        return self.commname

    class Meta:
        db_table = 'maintain_command'
        verbose_name = "命令列表"
        verbose_name_plural = verbose_name


class SshExecCommand(models.Model):
    tags = models.CharField("标签", max_length=32)
    host = models.CharField("主机ip", max_length=32)
    user = models.CharField("主机用户名", max_length=32)
    password = models.CharField("主机用户密码", max_length=255)
    sshport = models.IntegerField("主机ssh端口号", default=22)
    ssh_cmd = models.CharField('执行的命令', max_length=200)
    execresult = models.TextField("执行结果", max_length=5000, blank=True, null=True)
    createtime_ssh = models.DateTimeField("执行时间", default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'sshexec_command'
        verbose_name = "命令运行"
        verbose_name_plural = verbose_name


class UploadDownFileInfo(models.Model):
    file_name = models.CharField('文件名', max_length=500)
    file_size = models.CharField('文件大小', max_length=10, )
    file_path = models.CharField('文件传输路径', max_length=500)
    file_host = models.CharField('文件上传服务器地址', max_length=32)
    file_type = models.IntegerField('文件传输类型', default=1)  # 1上传 0下载2
    upload_time = models.DateTimeField('传输时间', default=timezone.now, blank=True, null=True)
    remarks = models.CharField('备注', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = 'upload_file'
        verbose_name = "文件上传"
        verbose_name_plural = verbose_name


class PortCheck(models.Model):
    tags = models.CharField("标签", max_length=32)
    host = models.CharField("主机ip", max_length=32)
    user = models.CharField("主机用户名", max_length=32)
    password = models.CharField("主机用户密码", max_length=255)
    sshport = models.IntegerField("主机ssh端口号", default=22)
    check_type = models.IntegerField('检查类型 0端口 1进程', default=0)  # 0是端口 1进程
    # 0:Tomcat 1:ftp 2:oracle 3:mysql 4:nginx 5:php 6:java  7:docker

    check_server = models.IntegerField("检查服务 0:Tomcat 1:ftp 2:oracle 3:mysql 4:nginx 5:php 6:java  7:docker", default=0)
    createtime_ssh = models.DateTimeField("执行时间", default=timezone.now, blank=True, null=True)
    operate_type = models.IntegerField('操作类型  0停止{查杀}、1启动，2重载', default=0)  # 0停止{查杀}、1启动，2重载

    def __str__(self):
        return True

    class Meta:
        db_table = 'portcheck'
        verbose_name = "端口检测"
        verbose_name_plural = verbose_name
