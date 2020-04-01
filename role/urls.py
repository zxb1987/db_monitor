from django.urls import path

from role import views

app_name = "role"

urlpatterns = [
    path('api/role-list', views.ApiRolelist.as_view()),
    path('api/role-list<int:pk>', views.ApiRoleDetail.as_view()),

]
