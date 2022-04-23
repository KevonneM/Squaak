from django.contrib import admin
from messaging.models import OnetoOneRoom, Message

# Register your models here.

admin.site.register(OnetoOneRoom)
admin.site.register(Message)