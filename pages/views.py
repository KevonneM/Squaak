from django.shortcuts import render
from django .views.generic import TemplateView

# Create your views here.

# HomePage View
class HomePageView(TemplateView):
    template_name = 'home.html'