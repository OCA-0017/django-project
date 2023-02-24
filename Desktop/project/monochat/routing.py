from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
#    path( 'ws/chat/', consumers.ChatConsumer.as_asgi() ),
    re_path(r'ws/monochat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]