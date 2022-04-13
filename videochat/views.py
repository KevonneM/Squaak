from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
# Create your views here.

def getToken(request):
    appId = 'e393edf6a2064a009f02a0dbd24284c5'
    appCertificate = 'd8ec4910ca4842f89ae7bdf7d8ef59e1'
    channelName = request.GET.get('channel')
    uid =  random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1   

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse ({'token':token, 'uid':uid}, safe=False)

def videochatlobbyviews(request):
    return render(request, 'videochatlobby.html')

def videochatroomviews(request):
    return render(request, 'videochatroom.html')