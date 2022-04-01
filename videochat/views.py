from django.shortcuts import render

# Create your views here.
def videochatlobbyviews(request):
    return render(request, 'videochatlobby.html')

def videochatroomviews(request):
    return render(request, 'videochatroom.html')