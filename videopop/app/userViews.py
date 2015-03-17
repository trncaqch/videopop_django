from django.shortcuts import render
from django.http import HttpResponse

def userProfile(request):
    return HttpResponse("UserProfile")
