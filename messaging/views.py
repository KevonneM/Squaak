from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from users.models import CustomUser
from messaging.models import OnetoOneRoom

from messaging.consumers import ChatConsumer
from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer

#since django runs synchronously and channel_layer runs asynchronous.
#we need to explicitly tell channel_layer to run it in synchronous.

# Create your views here.

# View for the Messaging page.
def messaging_page(request):
    return render(request, 'messenger.html', {
        'rooms': OnetoOneRoom.objects.all(),
    })

# View for the private chat room.
def private_chat_room(request, room_name):

    private_room, created = OnetoOneRoom.objects.get_or_create(name=room_name)
    
    return render(request, 'privatechat.html', {
        'room': private_room,
    })