from django.urls import path

from . import views

app_name = 'messaging'

urlpatterns = [
    path('messenger/', views.messaging_page, name='messenger'),
    path('messenger/chat_room/<str:room_name>/', views.chat_room, name='chat-room'),
]