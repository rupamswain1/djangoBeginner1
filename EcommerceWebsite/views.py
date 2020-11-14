from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ecommHome(request):
    return render(request,'ecommHome.html')

def ecommCart(request):
    return HttpResponse("Cart")

def ecommAboutUs(request):
    return HttpResponse("About US")

def ecommContactUs(request):
    return HttpResponse("Contact Us")

def ecommProductPage(request):
    return HttpResponse("Product Page")