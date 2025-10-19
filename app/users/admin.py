from django.contrib import admin
from .models import User, ClientProfile, FreelancerProfile
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
    
@admin.register(ClientProfile)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "bio",
        "company_name",
        "website",
        "location"
    ]
    
@admin.register(FreelancerProfile)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "bio",
        "hourly_rate",
        "years_experience",
        "rating"
    ]