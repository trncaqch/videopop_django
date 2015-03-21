from random import randint, shuffle
from django.shortcuts import render
from models import Video, Score
from django.http import HttpResponse, HttpResponseRedirect



oldanswer = ''
refreshes = -1
correctAnswers = 0


def play(request):
    video_list = []
    context_dict = {}
    global oldanswer
    global refreshes
    global correctAnswers

    if request.method == "POST":
        value = request.POST['submit']
        if value == oldanswer:
            correctAnswers += 1
    # if request.method == "GET":
    for x in xrange(0, 4):

        random_idx = randint(0, Video.objects.count() - 1)
        random_video = Video.objects.all()[random_idx]

        if random_video in video_list:
            random_idx = randint(0, Video.objects.count() - 1)
            random_video = Video.objects.all()[random_idx]

        video_list.append(random_video)

    src = "https://www.youtube.com/embed/" + video_list[0].videoid + "?autoplay=1&start=68"

    refreshes = refreshes + 1
    answer = video_list[0].correctAnswer
    oldanswer = answer
    shuffle(video_list)
    context_dict = {"source": src,
                    "videos": video_list,
                    "answers": answer,
    }

    if refreshes == 5:
        if request.user.is_authenticated():
            add_score(request.user, correctAnswers * randint(5, 10), correctAnswers, refreshes)
        refreshes = -1
        correctAnswers = 0
        return HttpResponseRedirect('/vidpop/results')

    return render(request, 'app/game.html', context_dict)


def add_score(user, score, correctAnswers, videosSeen):
    s = Score.objects.create(user=user)
    s.score = score
    s.correctAnswers = correctAnswers
    s.videosSeen = videosSeen
    s.save()
    return s