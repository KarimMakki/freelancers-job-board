from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'profile_picture')
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
        ('Profile Picture', {'fields': ('profile_picture',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
        ('Profile Picture', {'fields': ('profile_picture',)}),
    )
