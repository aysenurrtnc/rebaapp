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

    table_A = [[[1, 2, 3, 4], [2, 3, 4, 5], [2, 4, 5, 6], [3, 5, 6, 7], [4, 6, 7, 8]],
              [[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]],
              [[3, 3, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 9]]]

    table_B = [[[1, 2, 2], [1, 2, 3]],
              [[1, 2, 3], [2, 3, 4]],
              [[3, 4, 5], [4, 5, 5]],
              [[4, 5, 5], [5, 6, 7]],
              [[6, 7, 8], [7, 8, 8]],
              [[7, 8, 8], [8, 9, 9]],]

    table_C = [[1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7],
              [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8],
              [2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8],
              [3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9],
              [4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9],
              [6, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 10],
              [7, 7, 7, 8, 9, 9, 9, 10, 10, 11, 11, 11],
              [8, 8, 8, 9, 10, 10, 10, 10, 10, 11, 11, 11],
              [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12],
              [10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12],
              [11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12],
              [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],]
    
    # Table A
    neck_position = int(request.POST.get('neck_position'))
    if(request.POST.get('neck_adjustment')):
        neck_adjustment = int(request.POST.get('neck_adjustment'))
        neck_score = neck_position + neck_adjustment
    else:
        neck_score = neck_position

    trunk_position = int(request.POST.get('trunk_position'))
    if(request.POST.get('trunk_adjustment')):
        trunk_adjustment = int(request.POST.get('trunk_adjustment'))
        trunk_score = trunk_position + trunk_adjustment
    else:
        trunk_score = trunk_position

    leg_position = int(request.POST.get('leg_position'))
    if(request.POST.get('leg_adjustments')):
        leg_adjustments = int(request.POST.get('leg_adjustments'))
        leg_score = leg_position + leg_adjustments
    else:
        leg_score = leg_position

    posture_score_A = table_A[neck_score-1][trunk_score-1][leg_score-1]

    force_load = int(request.POST.get('force_load'))
    force_load2 = 0
    if(request.POST.get('force_load2')):
        force_load2 = int(request.POST.get('force_load2'))

    score_A = posture_score_A + force_load + force_load2

    # Table B
    upper_arm_position = int(request.POST.get('upper_arm_position'))
    upper_arm_score = upper_arm_position
    if(request.POST.get('upper_arm_adjustment1')):
        upper_arm_adjustment1 = int(request.POST.get('upper_arm_adjustment1'))
        upper_arm_score += upper_arm_adjustment1
    if(request.POST.get('upper_arm_adjustment2')):
        upper_arm_adjustment2 = int(request.POST.get('upper_arm_adjustment2'))
        upper_arm_score += upper_arm_adjustment2
    if(request.POST.get('upper_arm_adjustment3')):
        upper_arm_adjustment3 = int(request.POST.get('upper_arm_adjustment3'))
        upper_arm_score += upper_arm_adjustment3

    lower_arm_position = int(request.POST.get('lower_arm_position'))

    wrist_position = int(request.POST.get('wrist_position'))
    wrist_score = wrist_position
    if(request.POST.get('wrist_adjustment')):
        wrist_adjustment = int(request.POST.get('wrist_adjustment'))
        wrist_score += wrist_adjustment
    
    score_B = table_B[upper_arm_score-1][lower_arm_position-1][wrist_score-1]

    coupling = int(request.POST.get('coupling'))

    posture_score_B = score_B + coupling

    # Table C and final reba score
    score_C = table_C[score_A-1][score_B-1]

    final_reba_score = score_C
    if(request.POST.get('activity_score1')):
        activity_score1 = int(request.POST.get('activity_score1'))
        final_reba_score += activity_score1
    if(request.POST.get('activity_score2')):
        activity_score2 = int(request.POST.get('activity_score2'))
        final_reba_score += activity_score2
    if(request.POST.get('activity_score3')):
        activity_score3 = int(request.POST.get('activity_score3'))
        final_reba_score += activity_score3

    # Result text
    if final_reba_score == 1:
        result_text = "Negligible risk"
    elif final_reba_score == 2 or final_reba_score == 3:
        result_text = "Low risk, change may be needed"
    elif final_reba_score > 3 and final_reba_score < 8:
        result_text = "Medium risk, further investigation, change soon"
    elif final_reba_score > 7 and final_reba_score < 11:
        result_text = "High risk, investigate and implement change"
    else:
        result_text = "Very high risk, implement change"

    context = {
        'result_text': result_text,
        'final_score': final_reba_score,
    }

    return render(request, 'reba/rebaResults.html', context)
   
def getfile(request):
   return serve(request, 'File')

def about(request):
    return render(request, 'reba/about.html', {'title': 'About'})