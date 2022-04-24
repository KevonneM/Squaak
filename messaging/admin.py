from django.contrib import admin
from messaging.models import ChatRoom, Message

# Register your models here.

admin.site.register(ChatRoom)
admin.site.register(Message)