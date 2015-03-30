import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videopop.settings')

import django
django.setup()

from youName import getVideoName
from youParse import crawl
from app.models import Video, Score
from random import randint
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def populate():
    user1 = add_user("test1", "pass", "p@p.com")
    user2 = add_user("test2", "pass", "p@p.com")
    user3 = add_user("test3", "pass", "p@p.com")
    user4 = add_user("test4", "pass", "p@p.com")
    users = [user1, user2, user3, user4]

    # add a score for each user
    for user in users:
        correctAnswers = randint(0,9)
        score = randint(0,15)
        add_score(user, correctAnswers*score, correctAnswers, correctAnswers+2)
        
    # add a second score for each user
    for user in users:
        correctAnswers = randint(0,9)
        score = randint(0,15)
        add_score(user, correctAnswers*score, correctAnswers, correctAnswers+2)        

    # add a playlist of videos
    # needs to be in format:
    # https://www.youtube.com/watch?v=<VIDEO_ID>&list=<PLAYLIST_ID>
    videoList = crawl(
        "https://www.youtube.com/watch?v=CevxZvSJLk8&list=PLWRJVI4Oj4IaYIWIpFlnRJ_v_fIaIl6Ey"
        )
    
    for url in videoList:
        videoid = url.split("=")[1]
        name = getVideoName(videoid)
        add_video(name, videoid)
        print url
        
    
def add_video(name, videoid):
    v = Video.objects.get_or_create(name = name)[0]
    v.videoid = videoid
    v.save()
    return v

def add_score(user, score, correctAnswers, videosSeen):
    s = Score.objects.create(user=user)
    s.score = score
    s.correctAnswers = correctAnswers
    s.videosSeen = videosSeen
    s.save()
    return s

def add_user(username, password, email):
    u = User.objects.get_or_create(username=username)
    u = u[0]
    u.password = make_password(password)
    u.email = email
    u.save()
    return u


if __name__ == '__main__':
    print 'Starting VideoPop population script...'
    populate()
