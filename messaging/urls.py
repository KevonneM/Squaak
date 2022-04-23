from django.urls import path

from . import views

app_name = 'messaging'

urlpatterns = [
    path('messenger/', views.messaging_page, name='messenger'),
    path('messenger/private_chat_room/<str:room_name>/', views.private_chat_room, name='private-chat-room'),
]