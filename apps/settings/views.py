from django.shortcuts import render

from .models import Setting,About

# Create your views here.
def  index(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting": setting
    }
    return render(request, "settings/home.html", context)

def contact(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting": setting
    }
    return render(request, "settings/contact.html", context)


def about(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")

    context = {
        "setting": setting,
        "about": about,
    }
    return render(request, "settings/about.html", context)

def team(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting": setting
    }
    return render(request, "settings/team.html", context)

def gallery(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting": setting
    }
    return render(request, "settings/gallery.html", context)