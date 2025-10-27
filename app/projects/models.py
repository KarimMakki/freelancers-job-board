from django.db import models
from app.users.models import ClientProfile, FreelancerProfile 

class Project(models.Model):
    CATEGORIES_CHOICES = [
        ('web_development', 'Web Development'),
        ('app_development','App Development'),
        ('data_analysis','Data Analysis'),
        ('graphic_design','Graphic Design'),
        ('advertising','Advertising'),
        ('writing_and_translation', 'Writing And Translation')
    
    ]
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
        
    ]
    # Client Assigned to the Project
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    
    # Basic Info
    title = models.CharField(max_length=55)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES_CHOICES)
    
    # Budget & Timeline
    budget_min = models.DecimalField(max_digits=10, decimal_places=2)
    budget_max = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(blank=True, null=True)
    
    # Selected Freelancer for Project
    selected_freelancer = models.ForeignKey(
        FreelancerProfile,
        on_delete=models.SET_NULL,
        blank=True, 
        null=True,
        related_name='awarded_projects')
    
    # Additional Info
    created_at = models.DateTimeField(auto_now_add=True)
    skills_required = models.CharField(max_length=255, blank=True, null=True)
    
    
    def __str__(self):
        return self.title