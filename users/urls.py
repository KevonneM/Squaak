from django.urls import path, include
from .views import SignUpView

app_name = 'users'

urlpatterns = [
    # Url using Django auth.
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]