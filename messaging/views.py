from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# View for the Messaging page.
class MessengerView(TemplateView):
    template_name = 'message.html'