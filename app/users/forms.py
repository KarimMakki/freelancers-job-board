# Django forms for user registration
# These forms extend Django's built-in UserCreationForm to handle both client and freelancer registration

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ClientProfile, FreelancerProfile

class ClientRegisterForm(UserCreationForm):
    """
    Form for client registration.
    Extends UserCreationForm to include additional client-specific fields.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Basic user fields from UserCreationForm

    # Additional fields specific to clients
    bio = forms.CharField(widget=forms.Textarea, required=False)  # Textarea for longer text input
    company_name = forms.CharField(required=False)  # Optional company name
    website = forms.URLField(required=False)  # URLField automatically validates URL format
    location = forms.CharField(required=True)  # Required location field

    def save(self, commit=True):
        """
        Override the save method to:
        1. Create the User object with role='client'
        2. Create the associated ClientProfile with additional client data
        """
        # Create user but don't save to database yet (commit=False)
        user = super().save(commit=False)
        user.role = 'client'  # Set the user role to client
        
        if commit:
            user.save()  # Now save the user to database
            # Create the client profile with the additional form data
            ClientProfile.objects.create(
                user=user,  # Link the profile to the user
                bio=self.cleaned_data.get('bio'),  # Get validated form data
                company_name=self.cleaned_data.get('company_name'),
                website=self.cleaned_data.get('website'),
                location=self.cleaned_data.get('location'),
            )
        return user


class FreelancerRegisterForm(UserCreationForm):
    """
    Form for freelancer registration.
    Extends UserCreationForm to include additional freelancer-specific fields.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Basic user fields from UserCreationForm

    # Additional fields specific to freelancers
    title = forms.CharField(required=True)  # Professional title (e.g., "Web Developer")
    bio = forms.CharField(widget=forms.Textarea, required=True)  # Required bio in textarea
    hourly_rate = forms.IntegerField(required=True)  # Rate per hour
    years_experience = forms.IntegerField(required=True)  # Years of experience

    def save(self, commit=True):
        """
        Override the save method to:
        1. Create the User object with role='freelancer'
        2. Create the associated FreelancerProfile with additional freelancer data
        """
        # Create user but don't save to database yet (commit=False)
        user = super().save(commit=False)
        user.role = 'freelancer'  # Set the user role to freelancer
        
        if commit:
            user.save()  # Now save the user to database
            # Create the freelancer profile with the additional form data
            FreelancerProfile.objects.create(
                user=user,  # Link the profile to the user
                title=self.cleaned_data.get('title'),  # Get validated form data
                bio=self.cleaned_data.get('bio'),
                hourly_rate=self.cleaned_data.get('hourly_rate'),
                years_experience=self.cleaned_data.get('years_experience'),
                rating=0.0,  # Default rating for new freelancers
            )
        return user