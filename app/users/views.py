from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientRegisterForm, FreelancerRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register_client(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            messages.success(request, "Your client account has been created!")
            return redirect('home')
    else:
            form = ClientRegisterForm()
    context = {'form': form}
    return render(request, 'app/registration/register_client.html', context)
    

def register_freelancer(request):
    if request.method == 'POST':
        form = FreelancerRegisterForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            messages.success(request, "Your freelancer account has been created!")
            return redirect('home')
    else:
        form = FreelancerRegisterForm()
    context = {'form': form}
    return render(request, 'app/registration/register_freelancer.html', context)