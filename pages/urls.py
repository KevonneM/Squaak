from django.urls import path

from pages.views import HomePageView, ProfilePageView, FriendsPageView, MessagePageView, VideoChatView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('profile/friends/', FriendsPageView.as_view(), name='friends'),
    path('profile/message/', MessagePageView.as_view(), name='message'),
    path('profile/videochat/', VideoChatView.as_view(), name='videochat'),
]