from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve

from django.db.models import Q


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def rebaWithoutVideo(request):
    return render(request, 'blog/rebaWithoutVideo.html')

   
def getfile(request):
   return serve(request, 'File')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



