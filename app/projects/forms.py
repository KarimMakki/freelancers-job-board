from django import forms
from .models import Project

class ProjectsCreationForm(forms.ModelForm):
    """ 
    Form for Project Creation
    """

    class Meta:
        model = Project
        exclude = ['selected_freelancer', 'created_at', 'client']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
    