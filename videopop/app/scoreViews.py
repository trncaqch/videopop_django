from django.shortcuts import render
from django.http import HttpResponse

def scores(request):
    return HttpResponse("HighScores page")
