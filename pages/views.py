from django.shortcuts import render
from django.views.generic import TemplateView
from users.models import CustomUser
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

# HomePage View.
class HomePageView(TemplateView):
    template_name = 'home.html'

# View for the Profile page.
class ProfilePageView(TemplateView):
    template_name = 'profile.html'

# View for the Friends page.
class FriendsPageView(TemplateView):
    template_name = 'friends.html'

# View for the Messaging page.
class MessagePageView(TemplateView):
    template_name = 'message.html'

# View for the Video chat page.
class VideoChatView(TemplateView):
    template_name = 'videochat.html'