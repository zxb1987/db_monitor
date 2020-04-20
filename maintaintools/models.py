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
    ssh_cmd = models.CharField('执行的命令', max_length=200, blank=True)
    createtime_ssh = models.DateTimeField("执行时间", default=timezone.now, blank=True, null=True)
    execresult = models.TextField("执行结果", max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'sshexec_command'
        verbose_name = "命令运行"
        verbose_name_plural = verbose_name
