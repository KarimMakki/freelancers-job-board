from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ClientProfile, FreelancerProfile

class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    bio = forms.CharField(widget=forms.Textarea, required=False)
    company_name = forms.CharField(required=False)
    website = forms.URLField(required=False)
    location = forms.CharField(required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'client'
        if commit:
            user.save()
            ClientProfile.objects.create(
                user=user,
                bio=self.cleaned_data.get('bio'),
                company_name=self.cleaned_data.get('company_name'),
                website=self.cleaned_data.get('website'),
                location=self.cleaned_data.get('location'),
            )
        return user


class FreelancerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    title = forms.CharField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=True)
    hourly_rate = forms.IntegerField(required=True)
    years_experience = forms.IntegerField(required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'freelancer'
        if commit:
            user.save()
            FreelancerProfile.objects.create(
                user=user,
                title=self.cleaned_data.get('title'),
                bio=self.cleaned_data.get('bio'),
                hourly_rate=self.cleaned_data.get('hourly_rate'),
                years_experience=self.cleaned_data.get('years_experience'),
                rating=0.0,  # default value
            )
        return user