from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class FriendList(models.Model):
    # Relationship is one friends list per user.
    # Friends list is deleted when user is deleted.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")

    # List of friends.
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        """Used to add a new friend."""
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):
        """Used to remove a friend."""
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        """Used to unfriend someone."""
        remover_friends_list = self # Users friend list.

        remover_friends_list.remove_friend(removee) # Using previous function to remove account from friends list.

        # Accessing removee list to remove user from their friends.
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """Checks to see if this is a friend."""
        if friend in self.friends.all():
            return True
        return False

class FriendRequest(models.Model):
    """Friend request logic to issue friend request from sender to receiver."""

    # Sender and receiver can issue or approve multiple requests.
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")

    is_active = models.BooleanField(blank=True, null=False, default=True)

    # As soon as a friend request is issued a timestamp is created.
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """Used to accept a friend request."""
        """Sender and user will both update on accept."""
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """When setting 'is_active' is set to false, friend request is declined."""
        self.is_active = False
        self.save()

    def cancel(self):
        """From perspective of sender."""

        self.is_active = False
        self.save()