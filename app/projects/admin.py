from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "title",
        "description",
        "category",
        "budget_min",
        "budget_max",
        "deadline",
        "selected_freelancer",
        "created_at",
        "skills_required"
    ]