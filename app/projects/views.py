from django.shortcuts import render, redirect
from .forms import ProjectsCreationForm
from app.users.models import ClientProfile

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