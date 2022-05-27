from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import ListView
from users.models import CustomUser, Profile
from users.forms import CustomUserChangeForm, ProfileUpdateForm
from messaging.models import PrivateMessage

from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

# Create your views here.

# HomePage View.
def homepage_view(request):

    return render(request, 'home.html')

# View for the Profile page.
def myprofilepageview(request, pk):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('pages:my_profile', pk)

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

# View for search page.
class SearchView(ListView):
    model = CustomUser
    template_name = 'search.html'
    
    def get_queryset(self):
        
        query = self.request.GET.get('user_name')
        object_list = CustomUser.objects.filter(username__icontains=query)

        return object_list

@receiver(post_save, sender=PrivateMessage)
def message_to_noti(sender, instance, created, **kwargs):

    if created:
        current_user = CustomUser.objects.get(pk=instance.private_receiver.pk)
        msg_sender = instance.private_sender.username

        content = instance.content

        # Actor for notification is the sender.
        notify.send(instance.private_sender, verb='Message Created', msg_sender=msg_sender, recipient=current_user, description=content, action_object=instance)