from django.shortcuts import render
from .models import Blog
from apps.settings.models import Setting
# Create your views here.
def blog(request):
    setting = Setting.objects.latest("id")
    blog = Blog.objects.all()
    context = {
        "setting": setting,
        "blog": blog,
        
    }
    return render(request, "blog/blog.html", context)

def blog_detail(request,id):
    random_new = Blog.objects.all().order_by('?')
    setting = Setting.objects.latest("id")
    blog = Blog.objects.get(id=id)
    context = {
        "setting": setting,
        "blog": blog,
        "random_new": random_new,
        
    }
    return render(request, "blog/blog-details.html", context)
