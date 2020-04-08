# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the MIT License.
from django.views.generic import View
from django.shortcuts import render
from django.http.response import HttpResponseBadRequest

from assets.models import LinuxList



def web_ssh(request, h_id):
    host = LinuxList.objects.filter(pk=h_id).first()
    if not host:
         return HttpResponseBadRequest('unknown host')
    context = {'id': h_id, 'title': host.hostname}
    return render(request, 'web_ssh.html')

