from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from pages.views import SearchView
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('my-profile/<int:pk>/', views.myprofilepageview, name='my_profile'),
    path('user_search/', login_required(SearchView.as_view()), name='search'),
]
