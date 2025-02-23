from django.db import models
from django.contrib.auth.models import User

class ExpertProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_expert_profile')
    mobile_number = models.CharField(max_length=15)
    category = models.CharField(max_length=100)
    experience = models.TextField()
    photo = models.ImageField(upload_to='experts/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()
