from django.shortcuts import render

# Create your views here.
def ecommHome(request):
    return render(request,'ecommHome.html')