from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url('ws/webssh/<int:pk>', consumers.WebsshConsumer),
    url('ws/webssh/', consumers.WebsshConsumer),
]