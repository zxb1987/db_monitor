import cx_Oracle
import paramiko
import psutil
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from mysql.connector import connection
import json
import numpy as np
# import pandas as pd
from django.db import connection
import pymysql.cursors

from .models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from utils.tools import get_utctime, today, last_day
from utils.django_tools import NoPagination


class ApiMysqlStat(generics.ListCreateAPIView):
    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        return MysqlStat.objects.filter(status=0, tags=tags).order_by('-status')

    serializer_class = MysqlStatSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMysqlStatHis(generics.ListCreateAPIView):
    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        if start_time and end_time:
            start_time = get_utctime(start_time)
            end_time = get_utctime(end_time)
        else:
            # default data of 1 day
            end_time = today()
            start_time = last_day()
        return MysqlStatHis.objects.filter(tags=tags, check_time__gte=start_time, check_time__lte=end_time).order_by(
            'check_time')

    serializer_class = MysqlStatSerializer
    pagination_class = NoPagination
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.DjangoModelPermissions,)


# all instance
class ApiMysqlStatList(generics.ListCreateAPIView):
    queryset = MysqlStat.objects.get_queryset().order_by('-id')
    serializer_class = MysqlStatSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host', 'status')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiMysqlSlowquery(generics.ListCreateAPIView):
    queryset = MysqlSlowquery.objects.get_queryset().order_by('-id')
    serializer_class = MysqlSlowquerySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host',)
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)


def Mysql_Excute(request):
    if request.method == 'GET':
        return HttpResponse('{"status":"0","message":"后台判断返回失败!!","result":"null"}')
    elif request.method == 'POST':
        req = str(request.body, 'utf-8')
        print("前端的值：" + req)
        try:
            cursor = connection.cursor()
            cursor.execute(req)
            # cursor.commit()
            row = cursor.fetchall()
            # print(row)
            index = cursor.description
            # print(index)
            # 获取每条数据的ID
            # row_id = [x[0] for x in row]
            # print(row_id)
            # 获取列名
            column_list = {}
            for i in range(len(index) - 1):
                column_list[index[i][0]] = index[i]
            df = np.array(row)
            # print(column_list)
            data = []
            for res in df:
                data.append(dict(zip(column_list, list(res))))
            print(data)
            return JsonResponse(data, safe=False)
        except Exception as e:
            print(e)
            return HttpResponse('{"status":"0","message":"查询失败!!","result":"null"}')
    # 方式一
    # return HttpResponse(json.dumps(data),content_type="application/json")
    # 方式2
    # return JsonResponse(data,safe=False)

def logintoserver(request):
    # req = str(request.body, 'utf-8')
    req = json.loads(request.body)
    print(req)
    allval = []
    text_commd = ''
    try:
        for i in req:
            allval.append(i)
        for val in allval:
            host = val.get('host')
            sshport = val.get('sshport')
            user = val.get('user')
            password = val.get('password')
            # tags = val.get('tags')
            # 实例化SSHClient
            client = paramiko.SSHClient()
            # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接SSH服务端，以用户名和密码进行认证
            client.connect(hostname=host, port=sshport, username=user, password=password)
            # 打开一个Channel并执行命令
            # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值，get_pty=True 从服务器请求一个伪终端(默认' ' False ' ')。见“.Channel.get_pty”
            #ps auxww|grep mysqld|grep -v root|grep -v grep
            stdin, stdout, stderr = client.exec_command('ps -ef | grep mysql', get_pty=True)
            res, err = stdout.read().decode('utf-8'), stderr.read().decode('utf-8')
            print(res)

            # 获取所有pid
            # pids = psutil.pids()
            # print(pids)

            #mysql登录
            try:
                conn = pymysql.connect(host=host,user='root',password='root')
                print(conn)
                cursor = conn.cursor()
                #获取改服务器下的所有数据库名
                cursor.execute('show databases')
                result = cursor.fetchall()
                # print(result)

                #进入数据库，获取所有表
                allbase=[]
                tabs=[]
                for base in result:
                    for i in base:
                        allbase.append(i)
                for db in allbase:
                    dictdata = {}
                    # print(db)
                    connect_sql = 'use' + ' ' + db
                    cursor.execute(connect_sql)
                    cursor.execute('show tables')
                    tables = cursor.fetchall()  # 获得表名，返回数组
                    dictdata["base"] = db
                    datamsg = []
                    for tb in tables:
                        for tbs in tb:
                            datamsg.append(tbs)
                    dictdata["tables"] = datamsg
                    tabs.append(dictdata)

                cursor.close()
                conn.close()
                client.close()
                return HttpResponse(json.dumps(tabs),content_type="application/json",)
            except Exception as e:
                return HttpResponse('{"status":"0","message":"数据库连接失败!!","result":"null"}')
    except Exception as e:
        print(e)
        return HttpResponse('{"status":"0","message":"服务器登录失败!!","result":"null"}')