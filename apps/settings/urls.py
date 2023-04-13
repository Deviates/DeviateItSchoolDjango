from django.urls import path
from .views import index,contact,about,team,gallery,team_detail
urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('team', team, name="team"),
    path('team/<int:id>/', team_detail, name="team_detail"),
    path('gallery', gallery, name="gallery"),
]