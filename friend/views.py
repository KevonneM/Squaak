from django.shortcuts import get_object_or_404, render
from users.models import Profile, CustomUser
from .models import FriendList, FriendRequest

# Create your views here.

# profile page view for other users.
def otherprofilepageview(request, pk):
    
    user = get_object_or_404(CustomUser, pk=pk)

    return render(request, 'otherprofile.html', {'user': user})