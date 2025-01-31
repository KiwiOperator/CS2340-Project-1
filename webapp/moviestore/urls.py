from django.contrib.auth import views as auth_views
from django.urls import path

from .views import login_view, signup_view, success_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("success/", success_view, name="success"),
]
