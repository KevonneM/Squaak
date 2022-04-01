from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class FriendRequest(models.Model):
    """Friend request logic to issue friend request from sender to receiver."""

    # Sender and receiver can issue or approve multiple requests.
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")

    is_active = models.BooleanField(blank=True, null=False, default=True)

    # As soon as a friend request is issued a timestamp is created.
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.sender.username, self.receiver.username)