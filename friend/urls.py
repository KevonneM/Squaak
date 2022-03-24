from django.urls import path, include

from . import views

app_name = 'friend'

urlpatterns = [
    path('users/<int:pk>/', views.otherprofilepageview, name='profile_view'),
]