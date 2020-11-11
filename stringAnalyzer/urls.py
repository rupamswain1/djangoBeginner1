
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stringAnalyzer',views.stringAnalyzer,name='stringAnalyzer'),
    path('stringAnalyzerBootstrap',views.stringAnalyzerBootstrap,name='stringAnalyzerBootstrap'),

]
