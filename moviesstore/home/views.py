from django.shortcuts import render
from django.shortcuts import render
from movies.models import Movie, Review

def home_view(request):
    example_movies = Movie.objects.all()[:4]
    example_reviews = Review.objects.order_by('-date')[:4]
    return render(request, 'home/index.html', {'example_movies': example_movies, 'example_reviews': example_reviews})

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})