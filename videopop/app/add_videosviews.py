from random import choice, shuffle
from django.shortcuts import render
from models import Video
from django.http import HttpResponse, HttpResponseRedirect
from populate import *
from youName import *
from youParse import *


def add_videos(request):
    name_list = []
    context_dict = {}
    if request.method == 'POST':
        url = request.POST.get('youtube')
        populate(url)
        
        context_dict["message"] = "Playlist successfully added"
        
    return render(request, 'app/add_videos.html', context_dict)
