from django.urls import path
from .views import index,contact,about,team,gallery
urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('team', team, name="team"),
    path('gallery', gallery, name="gallery"),
]