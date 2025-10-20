from django.urls import path
from .views import register_client, register_freelancer

urlpatterns = [
    path("register/client", register_client, name='register_client'),
    path("register/freelancer", register_freelancer, name='register_freelancer')
]