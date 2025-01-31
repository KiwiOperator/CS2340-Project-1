from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login, name="login"),
    path('review/create/', views.create_review, name="create_review"),
    path('review/edit/<int:review_id>/', views.edit_review, name="edit_review"),
    path('review/delete/<int:review_id>/', views.delete_review, name="delete_review"),
]