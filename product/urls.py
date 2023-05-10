from django.contrib import admin
from django.urls import path,include
from .views import home,show


urlpatterns = [
   
    path('', home),
    path('show/', show),


]