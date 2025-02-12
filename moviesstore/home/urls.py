from django.urls import path
from . import views
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # Homepage must point to home_view
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'),
]