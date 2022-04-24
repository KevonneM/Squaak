from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from users.models import CustomUser
from messaging.models import ChatRoom

from messaging.consumers import ChatConsumer
from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer

#since django runs synchronously and channel_layer runs asynchronous.
#we need to explicitly tell channel_layer to run it in synchronous.

# Create your views here.

# View for the Messaging page.
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