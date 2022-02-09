from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView



# Create your views here.

class SignUpView(CreateView):
    # Logic for the signup form.
    # CustomUserCreation form will tell django to use this form and redirect to login page once signed up.
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('pages:home')