from django.urls import path, include
from .views import SignUpView, CustomPasswordChangeView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # Url using Django auth.
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    #Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(), name= "reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_comlete"),
    #password change
    path('password_change/', CustomPasswordChangeView.as_view(),name='change_password'),
]