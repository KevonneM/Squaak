from django.db import models
from django.conf import settings
from messaging.managers import ThreadManager
from users.models import CustomUser
import uuid

# Create your models here.

class ChatRoom(models.Model):
    """Logic and structure for the room between users."""

    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=CustomUser, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()
    
    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'

class PrivateChatRoom(models.Model):
    """Logic and structure for the room between users."""

    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=CustomUser, blank=True)
    chat_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()
    
    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'

class Message(models.Model):
    """Structure for messages."""
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Public Messages: {self.user.username}: {self.content} [{self.timestamp}]'

class PrivateMessage(models.Model):
    """Structure for messages."""
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    privateroom = models.ForeignKey(to=PrivateChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Private Messages: {self.user.username}: {self.content} [{self.timestamp}]'