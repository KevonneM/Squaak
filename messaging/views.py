from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from users.models import CustomUser
from messaging.models import ChatRoom, Message, PrivateChatRoom, PrivateMessage

#since django runs synchronously and channel_layer runs asynchronous.
#we need to explicitly tell channel_layer to run it in synchronous.

# Create your views here.

# View for the Messaging page.
@login_required
def messaging_page(request):

    return render(request, 'messenger.html', {
        'rooms': ChatRoom.objects.all(),
    })

# View for the private chat room.
def chat_room(request, room_name):

    room, created = ChatRoom.objects.get_or_create(name=room_name)
    
    return render(request, 'chatroom.html', {
        'room': room,
    })

# View to initiate a direct chat session with current user information.
# The initiator of a direct chat will always be set to the user1 field of each Private Chat Room object.
# If the current user == user2 of the object they will access that existing room.
@login_required
def direct_chat_room(request, pk):
    
    current_user = request.user
    other_user = CustomUser.objects.get(pk=pk)

    # If chat does not exist, create one with current user being user1.
    if not PrivateChatRoom.objects.filter(user1=request.user, user2=other_user).exists() and not PrivateChatRoom.objects.filter(user2=request.user, user1=other_user).exists():
        PrivateChatRoom.objects.create(user1=request.user, user2=other_user)

        user1chat = PrivateChatRoom.objects.get(user1=request.user, user2=other_user)

        return render(request, 'user1directchatroom.html', {
            'user1chat': user1chat,
        })

    # If chat does exist with the current user == user1 and the other_user == user2, join that chatroom.
    # Chat messages that are linked to the private room are passed to the template aswell.
    if PrivateChatRoom.objects.filter(user1=request.user, user2=other_user).exists():

        direct_chat = PrivateChatRoom.objects.get(user1=request.user, user2=other_user)
        chat_messages = []
        
        if request.user == direct_chat.user1:
            user1chat = PrivateChatRoom.objects.get(user1=request.user, user2=other_user)
            chat_messages = PrivateMessage.objects.filter(privateroom=direct_chat)
            return render(request, 'user1directchatroom.html', {
                'user1chat': user1chat,
                'chat_messages': chat_messages,
            })

    # If chat does exist with the current user == user2 and the other_user == user1, join that chatroom.
    # Chat messages that are linked to the private room are passed to the template aswell.
    if PrivateChatRoom.objects.filter(user2=request.user, user1=other_user).exists():

        direct_chat = PrivateChatRoom.objects.get(user2=request.user, user1=other_user)
        chat_messages = []
        
        if request.user == direct_chat.user2:
            user2chat = PrivateChatRoom.objects.get(user1=other_user, user2=request.user)
            chat_messages = PrivateMessage.objects.filter(privateroom=direct_chat)
            return render(request, 'user2directchatroom.html', {
                'user2chat': user2chat,
                'chat_messages': chat_messages,
            })

    else:
        raise Http404('User not authorized for this chatroom.')