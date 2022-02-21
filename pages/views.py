from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView
from users.models import Profile
from users.forms import CustomUserChangeForm, ProfileUpdateForm

# Create your views here.

# HomePage View.
class HomePageView(TemplateView):
    template_name = 'home.html'

# View for the Profile page.
def profilepageview(request, pk):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('pages:profile', pk)

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

# View for the Friends page.
class FriendsPageView(TemplateView):
    template_name = 'friends.html'

# View for the Messaging page.
class MessagePageView(TemplateView):
    template_name = 'message.html'

# View for the Video chat page.
class VideoChatView(TemplateView):
    template_name = 'videochat.html'