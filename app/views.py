from django.shortcuts import render
from app.projects.views import get_all_projects, get_recent_projects

# Create your views here.
def home(request):
    all_projects = get_all_projects()
    recent_projects = get_recent_projects()
    context = {
        'all_projects': all_projects,
        'recent_projects': recent_projects
    }
    return render(request, 'app/home.html', context)