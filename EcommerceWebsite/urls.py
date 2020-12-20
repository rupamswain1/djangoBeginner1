"""djangoBeginner1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.ecommHome,name='ecommHome'),
    path("cart/<int:product_id>/<str:operation>",views.ecommCart,name='ecommCart'),
    path("aboutUs/",views.ecommAboutUs, name='ecommAboutUs'),
    path("contactUs/",views.ecommContactUs, name='ecommContactUs'),
    path("productPage/<int:product_id>",views.ecommProductPage,name='ecommProductPage'),
    path("cart/", views.cart,name='cart'),
    path("search/", views.searchProduct, name='searchProduct'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout')
]
