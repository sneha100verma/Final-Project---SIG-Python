from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.home , name='project' ),
    path('pro1.html' , views.f1 , name = 'pro1'),
    path('pro2.html' , views.f2 , name = 'pro2'),
    path('pro3.html' , views.f3 , name = 'pro3')
]