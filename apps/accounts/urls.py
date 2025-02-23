from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_expert, name='register_expert'),
    path('registration-success/', views.registration_success, name='registration_success'),
]
