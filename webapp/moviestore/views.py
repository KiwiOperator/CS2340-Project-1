from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assign the logged-in user to the review
            review.save()
            return redirect('index')  # Redirect to the homepage after saving
    else:
        form = ReviewForm()
    return render(request, 'moviestore/create_review.html', {'form': form})

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
    return HttpResponse("Placeholder")

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'moviestore/login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('index')

    messages.error(request, 'Invalid username or password')
    return render(request, 'moviestore/login.html', {'form': form})