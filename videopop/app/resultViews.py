from django.shortcuts import render
from django.http import HttpResponse
from Models import Score

def results(request):
    context_dict = {}
    last_result = Score.object.
    return render(request, 'app/results.html')
