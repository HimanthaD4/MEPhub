from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # path('upcoming/', views.upcoming_projects, name='upcoming_projects'),
    path('', views.projects, name='projects'),
    
]
