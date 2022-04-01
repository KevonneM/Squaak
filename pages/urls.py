from django.urls import path, re_path

<<<<<<< HEAD
from pages.views import HomePageView, FriendsPageView, MessagePageView, SearchView
=======
from pages.views import HomePageView, MessagePageView, SearchView
>>>>>>> main
from . import views
app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
<<<<<<< HEAD
    path('<int:pk>/profile/', views.profilepageview, name='profile'),
    path('profile/friends/', FriendsPageView.as_view(), name='friends'),
    path('profile/message/', MessagePageView.as_view(), name='message'),
    path('user_search/', SearchView.as_view(), name='search'),
] 
=======
    path('my-profile/<int:pk>/', views.myprofilepageview, name='my_profile'),
    path('message/', MessagePageView.as_view(), name='message'),
    path('user_search/', SearchView.as_view(), name='search')
]
>>>>>>> main
