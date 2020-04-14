from django.http import HttpResponse
from django.shortcuts import render

from utils.mysql_base import MysqlBase
from utils.mysql_base import MysqlBase
from utils.linux_base import LinuxBase
from user.models import UserList
def hello(request):
    print(123)
    return HttpResponse('123')
