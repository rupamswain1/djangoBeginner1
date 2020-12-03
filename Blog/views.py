from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def blogHome(request):
    blogs=BlogPost.objects.all()
    return render(request,'blogHome.html',{'blogs':blogs})

def blogView(request,blog_id):
    blog=BlogPost.objects.get(blog_id)
    return render(request,'blogView.html')