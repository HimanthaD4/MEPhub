from django import forms
from django.contrib.auth.models import User
from .models import ExpertProfile

class ExpertRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = ExpertProfile
        fields = ['mobile_number', 'category', 'experience', 'photo']
