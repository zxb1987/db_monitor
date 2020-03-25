# encoding:utf-8
from django.db import models
from django.utils import timezone

# Create your models here.

# app监控列表
class AppList(models.Model):


    print("----------------models>UserList-----------------------")
    app_id = models.CharField("应用ID",max_length=32,blank=True,null=True)
    app_name = models.CharField("应用名称",max_length=32,blank=True,null=True)
    app_obj = models.CharField("项目名称",max_length=32,blank=True,null=True)
    remarks = models.CharField("备注", max_length=32, blank=True, null=True)
    check_time = models.DateTimeField("添加时间", default=timezone.now, blank=True, null=True)
    def __str__(self):
        return self.app_name



    class Meta:
        db_table = 'system_app'
        verbose_name = "app信息"
        verbose_name_plural = verbose_name

