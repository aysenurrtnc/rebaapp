from django.urls import path
from . import views
#http://127.0.0.1:8000
#http://127.0.0.1:8000/home

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("users", views.users),
    

   
]