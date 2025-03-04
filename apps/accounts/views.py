from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User

def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not all([full_name, email, phone, password, confirm_password]):
            messages.error(request, "All fields are required.")
            return redirect("accounts:register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("accounts:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("accounts:register")

        user = User.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            password=make_password(password),
        )
        messages.success(request, "Registration successful! You can now log in.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("accounts:login")

        if check_password(password, user.password):
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("/")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("accounts:login")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("/")
