# Generated by Django 3.0.3 on 2020-04-10 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppConfigSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.CharField(max_length=32, verbose_name='')),
                ('test2', models.CharField(max_length=32, verbose_name='')),
                ('test3', models.CharField(max_length=32, verbose_name='')),
            ],
            options={
                'verbose_name': 'app配置设置',
                'verbose_name_plural': 'app配置设置',
                'db_table': 'app_conf_setting',
            },
        ),
        migrations.CreateModel(
            name='AppList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(blank=True, max_length=32, null=True, verbose_name='应用ID')),
                ('app_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='应用名称')),
                ('app_host', models.CharField(max_length=32, verbose_name='应用归属服务器')),
                ('app_type', models.CharField(max_length=256, verbose_name='应用类型')),
                ('app_url', models.CharField(max_length=256, verbose_name='应用路径')),
                ('app_status', models.IntegerField(blank=True, null=True, verbose_name='应用连接状态 0离线 1成功')),
                ('app_obj', models.CharField(blank=True, max_length=32, null=True, verbose_name='项目名称')),
                ('remarks', models.CharField(blank=True, max_length=32, null=True, verbose_name='备注')),
                ('check_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': 'app信息',
                'verbose_name_plural': 'app信息',
                'db_table': 'system_app',
            },
        ),
    ]
