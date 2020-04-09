from django.db import models
from django.utils import timezone
from utils import tools


class MaintainCommand(models.Model):
    commname = models.CharField('命令名称', max_length=200)
    usecommand = models.CharField('执行命令', max_length=200, blank=True, null=True)
    commandparam = models.CharField('命令参数', max_length=20, blank=True)
    host = models.CharField("主机ip", max_length=32)
    hostname = models.CharField("主机名", max_length=64, blank=True, null=True)
    linux_version = models.CharField("linux版本", max_length=64, blank=True, null=True)
    createtime = models.DateTimeField("创建时间", default=timezone.now, blank=True, null=True)
    updatedtime = models.DateTimeField("更新时间", default=timezone.now, blank=True, null=True)
    remark = models.CharField('备注', max_length=200, blank=True)

    def __str__(self):
        return self.commname

    class Meta:
        db_table = 'maintain_command'
        verbose_name = "命令运行"
        verbose_name_plural = verbose_name
