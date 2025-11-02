from django.shortcuts import render, redirect
from .forms import ProjectsCreationForm
from app.users.models import ClientProfile
from django.utils import timezone
from datetime import timedelta
from app.projects.models import Project

def create_project(request):
    if request.method == 'POST':
        form = ProjectsCreationForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client =ClientProfile.objects.get(user=request.user)
            project.save()
            return redirect('home')  # Redirect to home after successful creation
    else:
        form = ProjectsCreationForm()
    context = {'form': form}
    return render(request,'app/client_pages/create_project.html', context)

def get_all_projects():
    
    projects = Project.objects.all()
    
    return projects
    

def get_recent_projects():
    # Calculate the date one week ago from now
    one_week_ago = timezone.now() - timedelta(days=7)

    # Filter projects created within the last 7 days
    recent_projects = Project.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    return recent_projects