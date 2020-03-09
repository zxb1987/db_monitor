# encoding:utf-8
from django.db import models

# Create your models here.

# linux监控列表
class LinuxList(models.Model):



    tags = models.CharField("标签",max_length=32,unique=True)
    host = models.CharField("主机ip",max_length=32)
    hostname = models.CharField("主机名",max_length=256)
    linux_version = models.CharField("linux版本",max_length=32,choices=LINUX_VERSION)
    linux_kernel = models.CharField("内核版本",max_length=64,blank=True,null=True)
    user = models.CharField("主机用户名",max_length=32)
    password = models.CharField("主机用户密码",max_length=255)
    sshport = models.IntegerField("主机ssh端口号",default=22)
    serialno = models.CharField("序列号",max_length=100,blank=True,null=True)
    status = models.IntegerField("状态",choices=STATUS,blank=True,null=True)
    cabinet = models.CharField("机柜",max_length=100,blank=True,null=True)
    factory = models.CharField("服务器厂家",max_length=100,blank=True,null=True)
    purchase_date = models.CharField("采购日期",max_length=32,blank=True,null=True)
    beginprotection_date = models.CharField("保修开始日期",max_length=32,blank=True,null=True)
    overprotection_date = models.CharField("过保日期",max_length=32,blank=True,null=True)
    bussiness_system = models.CharField("业务系统",max_length=255,blank=True,null=True)
    system_level = models.IntegerField("系统等级 0:核心系统 1:重要系统 2:一般系统",default=0)
    res_description = models.CharField("资源描述",max_length=255,blank=True,null=True)
    main_software = models.CharField("主要部署软件",max_length=255,blank=True,null=True)
    alarm_connect = models.IntegerField("通断告警",default=1)
    alarm_cpu = models.IntegerField("CPU使用率告警",default=1)
    alarm_mem = models.IntegerField("内存使用率告警",default=1)
    alarm_swap = models.IntegerField("swap使用率告警",default=1)
    alarm_disk = models.IntegerField("磁盘使用率告警",default=1)
    alarm_alert_log = models.IntegerField("后台日志告警",default=1)
    alert_log = models.CharField("后台日志路径",max_length=256,blank=True,null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'admin_user'
        verbose_name = "Linux主机"
        verbose_name_plural = verbose_name

