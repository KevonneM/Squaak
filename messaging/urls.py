from django.urls import path

from . import views
from .views import direct_chat_room

app_name = 'messaging'

urlpatterns = [
    path('messenger/', views.messaging_page, name='messenger'),
    path('messenger/chat_room/<str:room_name>/', views.chat_room, name='chat-room'),
    path('messenger/direct_chat/<int:pk>/', views.direct_chat_room, name='direct-chat'),
]