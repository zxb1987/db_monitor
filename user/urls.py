from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('api/user', views.ApiUserList.as_view()),
    path('api/user/<int:pk>', views.ApiUserDetail.as_view()),

]

