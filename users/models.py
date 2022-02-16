from re import A
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(null=True, blank=True)


class Profile(models.Model):

    REQUIRED_FIELDS = ('profile')

    profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()