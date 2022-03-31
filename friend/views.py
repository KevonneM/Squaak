from webbrowser import get
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile, CustomUser
from .models import FriendRequest
from django.contrib import messages

# Create your views here.

# profile page view for other users.
def otherprofilepageview(request, pk):
    
    user = get_object_or_404(CustomUser, pk=pk)
    current_user = request.user
    sent_friend_request = FriendRequest.objects.all()

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
    
    context = {
        'friends': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests
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

    user_account.friends.remove(friend_account)
    friend_account.friends.remove(user_account)

    return redirect('friend:friends')