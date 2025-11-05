
from django.contrib import admin
from .models import Bid

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = [
        "freelancer",
        "project",
        "bid_amount",
        "created_at",
    ]
    list_filter = ["created_at", "project"]
    search_fields = ["freelancer__user__username", "project__title"]
    readonly_fields = ["created_at"]