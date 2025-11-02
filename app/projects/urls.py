from django.urls import path
from app.projects import views
urlpatterns = [
    path("client/projects/create", views.create_project, name="create_project"),
    path("projects/<int:project_id>/", views.get_project_details, name="project_details"),
]