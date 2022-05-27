from django.urls import path, include
from .views import SignUpView, CustomPasswordChangeView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'users'

urlpatterns = [
    # Url using Django auth.
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    #Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ='registration/password_reset.html',
  email_template_name = 'registration/password_reset_email.html', success_url = reverse_lazy('users:password_reset_done')), name= "reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:login')),name="password_reset_confirm"),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_comlete"),
    #password change
    path('password_change/', CustomPasswordChangeView.as_view(),name='change_password'),
    path('delete_owner/', views.delete_owner, name="delete-owner"),
]