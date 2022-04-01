from django.urls import path, include

from . import views

app_name = 'friend'

urlpatterns = [
    
    path('users/<int:pk>/', views.otherprofilepageview, name='profile_view'),
    path('friends/', views.friends_list, name='friends'),
    path('send_friend_request/<int:pk>/', views.send_friend_request, name='send-friend-request'),
    path('cancel_friend_request/<int:pk>/', views.cancel_friend_request, name='cancel-friend-request'),
    path('accept_friend_request/<int:pk>/', views.accept_friend_request, name='accept-friend-request'),
    path('decline_friend_request/<int:pk>/', views.decline_friend_request, name='decline-friend-request'),
    path('delete_friend/<int:pk>/', views.delete_friend, name='delete-friend'),
]