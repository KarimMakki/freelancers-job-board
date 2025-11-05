from django.contrib import admin

from .users.admin import UserAdmin, ClientAdmin, FreelancerAdmin
from .projects.admin import ProjectAdmin
from .bids.admins import BidAdmin