from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve

from django.db.models import Q


def home(request):
    return render(request, 'reba/home.html')

def rebaWithoutVideo(request):
    return render(request, 'reba/rebaWithoutVideo.html')

def rebaWithVideo(request):
    return render(request, 'reba/rebaWithVideo.html')

def rebaResults(request):
    trunk_position = request.POST.get('trunk_position')
    final_score = 9
    result_text = f"High Risk this that"
    context = {
        'result_text': result_text,
        'final_score': final_score,
    }
    return render(request, 'reba/rebaResults.html', context)
   
def getfile(request):
   return serve(request, 'File')

def about(request):
    return render(request, 'reba/about.html', {'title': 'About'})



