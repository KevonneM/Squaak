from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from friend.models import FriendRequest
from users.models import CustomUser, Profile
from users.forms import CustomUserChangeForm, ProfileUpdateForm

# Create your views here.

# HomePage View.
class HomePageView(TemplateView):
    template_name = 'home.html'

# View for the Profile page.
def myprofilepageview(request, pk):
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

# View for the Messaging page.
class MessagePageView(TemplateView):
    template_name = 'message.html'

# View for search page.
class SearchView(ListView):
    model = CustomUser
    template_name = 'search.html'
    
    def get_queryset(self):
        
        query = self.request.GET.get('user_name')
        object_list = CustomUser.objects.filter(username__icontains=query)

        return object_list