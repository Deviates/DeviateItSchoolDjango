from django.shortcuts import render
from apps.settings.models import Setting
# Create your views here.

def course(request):
    setting = Setting.objects.latest("id")
    return render(request,'course/course-details.html', locals())