from django.urls import path

from messaging.views import MessengerView

app_name = 'messaging'

urlpatterns = [
    path('messenger/', MessengerView.as_view(), name='messenger'),
]