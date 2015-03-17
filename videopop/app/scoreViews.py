from django.shortcuts import render
from django.http import HttpResponse

def scores(request):
    return render(request, 'app/scores.html')
