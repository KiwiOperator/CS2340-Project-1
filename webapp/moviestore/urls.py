from django.contrib.auth import views as auth_views
from django.urls import path
from .views import homepage, login_view, signup_view, success_view, create_review, edit_review, delete_review, index, review_page  # Add review_page here

urlpatterns = [
    path("", index, name="index"),
    path('homepage/', homepage, name="homepage"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("success/", success_view, name="success"),
    path('review_page/', review_page, name="review_page"),  # Add this line for the review page
    path('review/create/', create_review, name="create_review"),
    path('review/edit/<int:review_id>/', edit_review, name="edit_review"),
    path('review/delete/<int:review_id>/', delete_review, name="delete_review"),
]