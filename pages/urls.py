from django.urls import path, re_path

from pages.views import HomePageView, FriendsPageView, MessagePageView, VideoChatView, SearchView
from . import views

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-profile/<int:pk>/', views.myprofilepageview, name='my_profile'),
    path('friends/', FriendsPageView.as_view(), name='friends'),
    path('message/', MessagePageView.as_view(), name='message'),
    path('videochat/', VideoChatView.as_view(), name='videochat'),
    path('user_search/', SearchView.as_view(), name='search')
]