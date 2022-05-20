from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class PrivateVideoChatRoom(models.Model):
    """Logic and structure for the room between users."""

    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)

    # videouser1 and videouser2 can initiate multiple direct videochat rooms.
    videouser1 = models.ForeignKey(settings.AUTH_USER_MODEL, default="", editable=False, on_delete=models.CASCADE, related_name="videouser1")
    videouser2 = models.ForeignKey(settings.AUTH_USER_MODEL, default="", editable=False, on_delete=models.CASCADE, related_name="videouser2")

    # Universally Unique Identifier for each Private Video Chat Room instance involving the fields above.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return "VideoChat between: {} and {}".format(self.videouser1.username, self.videouser2.username)