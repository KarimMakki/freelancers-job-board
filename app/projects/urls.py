from django.urls import path
from app.projects import views
urlpatterns = [
    path("client/projects/create", views.create_project, name="create_project")
]