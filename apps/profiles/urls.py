from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('detail/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('search/', views.search_results, name='search_results'),
]
