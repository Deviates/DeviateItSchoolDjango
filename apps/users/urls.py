from django.urls import path
from django.contrib.auth.views import LogoutView  
from .views import register, us_login,profile
# from .views import
urlpatterns = [
    path("register", register, name="register"),
    path("login", us_login, name="login"),
    path("profile", profile, name="profile"),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
]