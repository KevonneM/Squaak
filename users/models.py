from django.db import models
from django.contrib.auth.models import AbstractUser
from friend.models import FriendRequest

from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image
from autoslug import AutoSlugField

# User model inheriting from Django's AbstractUser.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    friends = models.ManyToManyField("CustomUser", blank=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    slug = AutoSlugField(populate_from='user', null=True)
    bio = models.TextField(max_length=250, default='Bio')
    

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        return "/profile/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)

# User profile is created upon user signup.
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# User profile is saved upon user signup.
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()