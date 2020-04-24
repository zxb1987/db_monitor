from django.urls import path

from maintaintools import views

app_name = "maintaintools"

urlpatterns = [
    path('api/command-list', views.ApiMaintainCommandList.as_view()),
    path('api/command-list/<int:pk>', views.ApiMaintainCommandDetail.as_view()),
    path('sshclient/<int:ssh_id>', views.GetPaerm.as_view()),
    path('api/uploaddownfile-list', views.ApiUploadDownFileList.as_view()),
    path('uploadfile/', views.ApiUploadDownFileList.uploadfile)
]
