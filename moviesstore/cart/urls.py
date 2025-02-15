from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:movie_id>/', views.remove_movie, name='remove_movie'),  # ✅ Correct name
    path('<int:id>/add/', views.add, name='add'),
    path('clear/', views.clear, name='clear'),
    path('purchase/', views.purchase, name='purchase'),
]