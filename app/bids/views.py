from django.shortcuts import render, redirect, get_object_or_404
from app.users.models import FreelancerProfile
from app.projects.models import Project
from .models import Bid
from .forms import BidForm
from django.contrib import messages
from django.db import IntegrityError

def add_bid(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to place a bid."),
            return redirect('login')  # Redirect to login page if not authenticated
        if request.user.role != 'freelancer':
            messages.error(request, 'Only freelancers can place bids.')
        else:
            try:
                freelancer_profile = FreelancerProfile.objects.get(user=request.user)
                form = BidForm(request.POST)
                if form.is_valid():
                    bid = form.save(commit=False)
                    bid.freelancer = freelancer_profile                  
                    bid.project = project
                    try:
                        bid.save()
                    except IntegrityError:
                        messages.error(request, 'You have already placed a bid for this project.')
                        return redirect('project_details', project.id)
                    messages.success(request, 'Bid placed successfully!')
                    return redirect('project_details', project.id)  # Redirect to project details page after successful bid
                else:
                    messages.error(request, 'Invalid bid form submission.')
            except FreelancerProfile.DoesNotExist:
                messages.error(request, 'Freelancer profile not found.')
                return redirect('home')  # Redirect to home if profile not found
    else:
        form = BidForm()
    context = {'form': form, 'project': project}
        
    return render(request, 'app/freelancer_pages/add_bid.html', context)