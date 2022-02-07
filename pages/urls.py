from django.urls import path

from pages.views import HomePageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]