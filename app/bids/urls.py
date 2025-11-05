from django.urls import path
from app.bids import views

urlpatterns = [
    path("projects/<int:project_id>/add-bid/", views.add_bid, name='add_bid'),
]