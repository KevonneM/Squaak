from django.urls import path
from .views import SignUpView

app_name = 'users'

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]