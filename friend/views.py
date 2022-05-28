from webbrowser import get
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from messaging.models import PrivateChatRoom
from videochat.models import PrivateVideoChatRoom
from users.models import Profile, CustomUser
from .models import FriendRequest
from django.contrib import messages

# Create your views here.

# profile page view for other users.
def otherprofilepageview(request, pk):
    
    user = get_object_or_404(CustomUser, pk=pk)
    current_user = request.user
    sent_friend_request = FriendRequest.objects.filter(sender=current_user, receiver=user)

    context = {
        'user': user,
        'current_user': current_user,
        'sent_friend_request': sent_friend_request
    }

    return render(request, 'otherprofile.html', context)

# View for the users Friends list.
def friends_list(request):

    p = request.user
    friends = p.friends.all()

    sent_friend_requests = FriendRequest.objects.filter(sender=request.user)
    rec_friend_requests = FriendRequest.objects.filter(receiver=request.user)

    initiated_direct_chats = PrivateChatRoom.objects.filter(user1=request.user)
    received_direct_chats = PrivateChatRoom.objects.filter(user2=request.user)

    initiated_video_chats = PrivateVideoChatRoom.objects.filter(videouser1=request.user)
    received_video_chats = PrivateVideoChatRoom.objects.filter(videouser2=request.user)
    
    context = {
        'friends': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,

        'initiated_direct_chats': initiated_direct_chats,
        'received_direct_chats': received_direct_chats,

        'initiated_video_chats': initiated_video_chats,
        'received_video_chats': received_video_chats,
    }
    return render(request, "friends.html", context)

# Function for sending a friend request.
@login_required
def send_friend_request(request, pk):

    sender = request.user
    receiver = CustomUser.objects.get(pk=pk)

    friend_request, created = FriendRequest.objects.get_or_create(sender=sender, receiver=receiver)

    if created:
        return redirect('friend:profile_view', pk=pk)
    else:
        return redirect('friend:profile_view', pk=pk)

# Function for cancelling a sent friend request.
def cancel_friend_request(request, pk):

    sender = request.user
    receiver = CustomUser.objects.get(pk=pk)

    friend_request = FriendRequest.objects.get(sender=sender, receiver=receiver)

    if friend_request.sender == request.user:
        friend_request.delete()
        messages.success(request, 'Friend Request Canceled.')
        return redirect('friend:profile_view', pk=pk)

# Function for accepting a friend request.
@login_required
def accept_friend_request(request, pk):

    friend_request = FriendRequest.objects.get(pk=pk)

    if friend_request.receiver == request.user:
        friend_request.receiver.friends.add(friend_request.sender)
        friend_request.sender.friends.add(friend_request.receiver)
        friend_request.delete()
        return redirect('friend:friends')
    else:
        decline_friend_request()

# Function for declining a friend request.
@login_required
def decline_friend_request(request, pk):

    friend_request = FriendRequest.objects.get(pk=pk)

    if friend_request.receiver == request.user:
        friend_request.delete()
        return redirect('friend:friends')
    else:
        accept_friend_request()

@login_required
def delete_friend(request,pk):

    user_account = request.user
    friend_account = CustomUser.objects.get(pk=pk)

    existing_messenger_initiated = PrivateChatRoom.objects.filter(user1=request.user, user2=friend_account)
    existing_messenger_received = PrivateChatRoom.objects.filter(user2=request.user, user1=friend_account)

    existing_videochat_initiated = PrivateVideoChatRoom.objects.filter(videouser1=request.user, videouser2=friend_account)
    existing_videochat_received = PrivateVideoChatRoom.objects.filter(videouser2=request.user, videouser1=friend_account)

    user_account.friends.remove(friend_account)
    friend_account.friends.remove(user_account)

    existing_messenger_initiated.delete()
    existing_messenger_received.delete()

    existing_videochat_initiated.delete()
    existing_videochat_received.delete()

    return redirect('friend:friends')