from django.contrib import admin
from friend.models import FriendRequest

# Register your models here.

class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender__username', 'sender__email', 'receiver__username', 'receiver__email']
    readonly_fields = ['sender', 'receiver']

    class Meta:
        model = FriendRequest

admin.site.register(FriendRequest, FriendRequestAdmin)