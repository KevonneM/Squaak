from django.urls import path, re_path

from pages.views import SearchView
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('my-profile/<int:pk>/', views.myprofilepageview, name='my_profile'),
    path('user_search/', SearchView.as_view(), name='search'),
]
