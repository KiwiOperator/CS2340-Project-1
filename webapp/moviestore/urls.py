from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login, name="login"),
    path('homepage/', views.homepage, name="homepage"),

    # path('logout/', views.logout, name="logout"),
    # path('signup/', views.signup, name="signup"),
]