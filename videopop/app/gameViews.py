from django.shortcuts import render
from django.http import HttpResponse
from models import Video
from random import randint, shuffle

def play(request):
    video_list = []
    for x in xrange(0, 4):
        random_idx = randint(0, Video.objects.count() - 1)
        video_list.append(Video.objects.all()[random_idx])
    src = "https://www.youtube.com/embed/" + video_list[0].videoid +"?autoplay=1&start=68"
    answer = video_list[0].correctAnswer        
    shuffle(video_list)
    context_dict = {"source" : src, "videos" : video_list, "answer" : answer}
    
    return render(request, 'app/game.html', context_dict)
