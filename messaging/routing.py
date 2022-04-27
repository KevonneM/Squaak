from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/messenger/chat_room/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/messenger/direct_chat/(?P<username>[\w.@+-]+)', consumers.DirectChatConsumer.as_asgi()),
]