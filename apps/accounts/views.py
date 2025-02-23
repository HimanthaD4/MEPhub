from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    # Render the login template
    return render(request, 'accounts/login.html')

def register_expert(request):
    # Render the registration form
    if request.method == "POST":
        # Process form data (to be implemented)
        return redirect('accounts:registration_success')
    return render(request, 'accounts/register_expert.html')

def registration_success(request):
    return render(request, 'accounts/registration_success.html')
