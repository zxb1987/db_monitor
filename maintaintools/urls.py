from django.urls import path

from maintaintools import views
from maintaintools import tests

app_name = "maintaintools"

urlpatterns = [
    path('api/command-list', views.ApiMaintainCommandList.as_view()),
    path('api/command-list/<int:pk>', views.ApiMaintainCommandDetail.as_view()),
    # path('sshclient/<int:pk>', views.ApiSSHClient)
    path('sshclient/<int:r_id>', views.GetPaerm.as_view())
]
