from django.db import models
from app.projects.models import Project
from app.users.models import FreelancerProfile

class Bid(models.Model):
    """Bid placed by a freelancer on a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bids')
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name='bids')
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(help_text="Explain why you're the best fit for this project")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        constraints = [
        models.UniqueConstraint(fields=['project', 'freelancer'],
                                name='unique_bid_per_project')
        ]  # A freelancer can only bid once per project
    
    def __str__(self):
        return f"{self.freelancer.user.username} - ${self.bid_amount} on {self.project.title}"