from django.urls import path
from app.users import views

urlpatterns = [
    path("register/client", views.register_client, name='register_client'),
    path("register/freelancer", views.register_freelancer, name='register_freelancer'),
    path("login/", views.login_user, name="login")
]