from django.urls import path, re_path

from pages.views import HomePageView, MessagePageView, SearchView
from . import views

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-profile/<int:pk>/', views.myprofilepageview, name='my_profile'),
    path('message/', MessagePageView.as_view(), name='message'),
    path('user_search/', SearchView.as_view(), name='search')
]