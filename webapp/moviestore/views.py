from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Import the custom form

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "moviestore/success.html")  # Show success message after login
        else:
            print("Login errors:", form.errors)  # Debugging login failures
    else:
        form = AuthenticationForm()
    return render(request, "moviestore/login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # Use custom form here
        if form.is_valid():
            user = form.save(commit=False)  # Create user but don’t save yet
            user.set_password(form.cleaned_data["password1"])  # Set the password manually
            user.save()  # Now save the user
            return redirect("login")  # Redirect to login page after successful signup
        else:
            print("Signup errors:", form.errors)  # Debugging signup failures
    else:
        form = CustomUserCreationForm()  # Initialize custom form
    return render(request, "moviestore/signup.html", {"form": form})

@login_required
def success_view(request):
    return render(request, "moviestore/success.html")
