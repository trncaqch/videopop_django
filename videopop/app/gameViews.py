from random import choice, shuffle
from django.shortcuts import render
from models import Video, Score
from django.http import HttpResponse, HttpResponseRedirect
import time

refreshes = -1
old_answer = ''
correctAnswers = 0
vidStart = time.time()
gameStart = time.time()
score = 0
blacklist = []

def play(request):
    # fields
    play_list = []
    global blacklist
    global vidStart
    global oldanswer
    global refreshes
    global correctAnswers
    global gameStart
    global score
    time_left = 30 - (int(time.time()) - int(gameStart))

    # if its the first time the game is started
    # this should definitely be a function
    if (refreshes < 0) or (int(time.time() - vidStart) > 5):
        restart()
        time_left = 30


    if request.method == "POST":
        points = 5 - round(time.time() - vidStart, 2)
        value = request.POST['submit']
        if value == oldanswer:
            correctAnswers += 1
            score = score + points
        else:
            time_left = time_left - int(points)

    # if request.method == "GET":

    video_list = Video.objects.all()

    for x in xrange(0, 4):
        random_video = choice(video_list)
        if x == 0:
            blacklist.append(random_video)
        if random_video in blacklist:
            random_video = choice(video_list)

        play_list.append(random_video)

    src = "https://www.youtube.com/embed/" + play_list[0].videoid + "?autoplay=1&start=68"

    refreshes = refreshes + 1
    answer = play_list[0].correctAnswer
    old_answer = answer
    shuffle(play_list)
    context_dict = {"source": src,
                    "videos": play_list,
                    "answers": answer,
                    "timeleft": time_left
    }

    if time_left <= 0:
        if request.user.is_authenticated():
            add_score(request.user, score, correctAnswers, refreshes)
        gameStart = time.time()
        refreshes = -1
        correctAnswers = 0
        return HttpResponseRedirect('/vidpop/results')

    print int(time.time() - vidStart)
    print time_left
    vidStart = time.time()
    print score
    return render(request, 'app/game.html', context_dict)

def restart():
    global refreshes
    refreshes = -1
    global oldanswer
    oldanswer = ''
    global correctAnswers
    correctAnswers = 0
    global vidStart
    vidStart = time.time()
    global gameStart
    gameStart = time.time()
    global score
    score = 0
    global blacklist
    blacklist = []

def add_score(user, score, correctAnswers, videosSeen):
    s = Score.objects.create(user=user)
    s.score = score
    s.correctAnswers = correctAnswers
    s.videosSeen = videosSeen
    s.save()
    return s

