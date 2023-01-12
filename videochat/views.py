from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time

import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

from users.models import CustomUser
from videochat.models import PrivateVideoChatRoom
# Create your views here.

def getToken(request):
    appId = config.get('appId')
    appCertificate = config.get('appCertificate')
    channelName = request.GET.get('channel')
    uid =  random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1   

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse ({'token':token, 'uid':uid}, safe=False)

@login_required
def videochatlobbyviews(request):
    return render(request, 'videochatlobby.html')

@login_required
def videochatroomviews(request):
    return render(request, 'videochatroom.html')

# View to initiate a direct videochat session with current user information.
# The initiator of a direct videochat will always be set to the videouser1 field of each Private VideoChat Room object.
# If the current user == user2 of the object they will access that existing room.
@login_required
def private_video_chat_room(request, pk):

    current_user = request.user
    other_user = CustomUser.objects.get(pk=pk)

    # If Videochat does not exist, create one with current user being videouser1.
    if not PrivateVideoChatRoom.objects.filter(videouser1=request.user, videouser2=other_user).exists() and not PrivateVideoChatRoom.objects.filter(videouser2=request.user, videouser1=other_user).exists():
        PrivateVideoChatRoom.objects.create(videouser1=request.user, videouser2=other_user)

        user1videochat = PrivateVideoChatRoom.objects.get(videouser1=request.user, videouser2=other_user)

        return render(request, 'privatevideo1.html', {
            'user1videochat': user1videochat,
        })

    # If chat does exist with the current user == videouser1 and the other_user == videouser2, join that chatroom.
    if PrivateVideoChatRoom.objects.filter(videouser1=request.user, videouser2=other_user).exists():

        direct_video_chat = PrivateVideoChatRoom.objects.get(videouser1=request.user, videouser2=other_user)

        if request.user == direct_video_chat.videouser1:
            user1videochat = PrivateVideoChatRoom.objects.get(videouser1=request.user, videouser2=other_user)

            return render(request, 'privatevideo1.html', {
                'user1videochat': user1videochat,
            })

    # If chat does exist with the current user == videouser2 and the other_user == videouser1, join that chatroom.
    if PrivateVideoChatRoom.objects.filter(videouser2=request.user, videouser1=other_user).exists():

        direct_video_chat = PrivateVideoChatRoom.objects.get(videouser2=request.user, videouser1=other_user)

        if request.user == direct_video_chat.videouser2:
            user2videochat = PrivateVideoChatRoom.objects.get(videouser1=other_user, videouser2=request.user)

            return render(request, 'privatevideo2.html', {
                'user2videochat': user2videochat,
            })

    else:
        raise Http404('User not authorized for this videochat room.')