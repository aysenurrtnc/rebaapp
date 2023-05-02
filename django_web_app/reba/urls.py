from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reba-home'),
    path('about/', views.about, name='reba-about'),
    path('rebaWithoutVideo/', views.rebaWithoutVideo, name='reba-rebaWithoutVideo'),

]
