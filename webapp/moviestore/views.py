from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from .models import Movie

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

def homepage(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10);
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'moviestore/movie_list.html', {'page_obj': page_obj})
