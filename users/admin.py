from django.contrib import admin
from .models import Profile, CustomUser

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username']

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['user__username']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)