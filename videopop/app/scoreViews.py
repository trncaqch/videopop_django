from django.shortcuts import render
from django.http import HttpResponse
from models import Score

def scores(request):
    score_list = Score.objects.order_by('-score')
    context_dict = { 'scores' : score_list}
    return render(request, 'app/scores.html', context_dict)
