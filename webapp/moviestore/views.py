from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CustomUserCreationForm  # Import the custom form
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Movie
from .forms import ReviewForm
from django.core.paginator import Paginator

@login_required
def review_page(request):
    reviews = Review.objects.filter(user=request.user)  # Show only the logged-in user's reviews
    return render(request, 'moviestore/review_page.html', {'reviews': reviews})

@login_required
def create_review(request):
    movie_title = request.GET.get('movie_title', '')
    reviews = Review.objects.filter(movie_title=movie_title)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assign the logged-in user to the review
            review.save()
            return redirect('index')  # Redirect to the homepage after saving
    else:
        form = ReviewForm(initial={'movie_title': movie_title})
    return render(request, 'moviestore/create_review.html', {'form': form, 'reviews': reviews})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)  # Ensure the user owns the review
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the homepage after saving
    else:
        form = ReviewForm(instance=review)
    return render(request, 'moviestore/edit_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)  # Ensure the user owns the review
    if request.method == 'POST':
        review.delete()
        return redirect('index')  # Redirect to the homepage after deleting
    return render(request, 'moviestore/confirm_delete.html', {'review': review})

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('review_page')  # Redirect logged-in users to the review page
    return render(request, 'moviestore/index.html')  # Render the homepage for non-logged-in users

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
            #return render(request, "moviestore/success.html")  # Show success message after login
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
    return redirect('homepage')

def custom_login_required(view_func):
    decorated_view_func = login_required(view_func, login_url='login_required')
    return decorated_view_func

@custom_login_required
def homepage(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
    paginator = Paginator(movies, 10);
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'moviestore/movie_list.html', {'page_obj': page_obj, 'username': request.user.username})

def login_required_view(request):
    return render(request, 'moviestore/loginrequired.html')