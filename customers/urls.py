from django.urls import path
from . import views #this point mean that is in the same directory

urlpatterns = [
    path('home',views.home, name="home"),
    path('aboutUs',views.aboutUs, name="aboutUs"),
    path('services',views.aboutUs, name="services"),
    path('contact',views.aboutUs, name="contact"),
   
]