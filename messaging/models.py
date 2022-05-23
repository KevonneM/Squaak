from django.db import models
from django.conf import settings
from django.forms import IntegerField
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
    
    # user1 and user2 can initiate multiple direct chat rooms.
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user2")

    # Universally Unique Identifier for each Private Chat Room instance involving the fields above.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()
    
    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return "DirectChat between: {} and {}".format(self.user1.username, self.user2.username)

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
    private_sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='private_sender')
    private_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='private_receiver')
    privateroom = models.ForeignKey(to=PrivateChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Private Message From: {self.private_sender.username}: {self.content} [{self.timestamp}] to {self.private_receiver.username} | Post ID: {self.id}'