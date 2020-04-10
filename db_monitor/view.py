from django.http import HttpResponse
from django.shortcuts import render

from utils.mysql_base import MysqlBase
from utils.mysql_base import MysqlBase
from utils.linux_base import LinuxBase
from user.models import UserList


def hello(request):

    mysql_params = {
        'host': '114.116.16.6',
        'port': 3306,
        'user': 'root',
        'password': 'jxnet_123qwe'
    }
    sql = "show DATABASES"


    testdate = MysqlBase(mysql_params).query(sql)

    queryset = UserList.objects.get_queryset()

    #UserList.objects.create(name="John Fourkas").save()
    #LinuxBase.connection().

    lucifer = UserList.objects.create(user_name="luciferdfd").save()


    print('===========================send=1===========================================')
    print(queryset)
    for querysetinfo in queryset:
        print(querysetinfo.department)
    print('===========================end==2==========================================')
    return render(request, 'web_ssh.html')
