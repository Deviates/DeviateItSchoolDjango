from django.shortcuts import render
from django.core.paginator import Paginator

from apps.blog.models import Blog
from .models import Setting,About,AboutNumber,Team,Gallery,Slide

# Create your views here.
def  index(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    number = AboutNumber.objects.latest("id")
    team = Team.objects.all().order_by('?')
    team_paginator = Paginator(team, 3)
    team_page_number = request.GET.get('page')
    team_page_number = team_paginator.get_page(team_page_number)
    blog = Blog.objects.all().order_by('?')
    blog_paginator = Paginator(blog, 3)
    blog_page_number = request.GET.get('page')
    blog_page_obj = blog_paginator.get_page(blog_page_number)
    slide = Slide.objects.latest("id")
    
    context = {
        "setting": setting,
        "about": about,
        "number": number,
        "team_page_number": team_page_number,
        "blog_page_obj": blog_page_obj,
        "slide": slide,

    }
    return render(request, "settings/home.html", context)

def contact(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting": setting,
    }
    return render(request, "settings/contact.html", context)


def about(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    number = AboutNumber.objects.latest("id")

    context = {
        "setting": setting,
        "about": about,
        "number": number,
    }
    return render(request, "settings/about.html", context)

def team(request):
    setting = Setting.objects.latest("id")
    team = Team.objects.all()

    context = {
        "setting": setting,
        "team": team,
    }
    return render(request, "settings/team.html", context)

def team_detail(request,id):
    setting = Setting.objects.latest("id")
    team = Team.objects.get(id=id)
    context = {
        "setting": setting,
        "team": team,
    }
    return render(request, "settings/team-details.html", context)

def gallery(request):
    setting = Setting.objects.latest("id")
    gallery = Gallery.objects.all()
    context = {
        "setting": setting,
        "gallery": gallery,
    }
    return   render(request, "settings/gallery.html", context)

