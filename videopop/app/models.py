import ast
import datetime
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    score = models.IntegerField(max_length=128)

    def __unicode__(self):
        return self.user.name

class Video(models.Model):
    name = models.CharField(max_length=128)
    videoid = models.CharField(max_length=128)


class Game(models.Model):
    game_mode = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    url = models.ForeignKey(Video)

    def __unicode__(self):
        return self.game_mode


class Score(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    score = models.DecimalField(default=0, max_digits = 7, decimal_places = 2)
    correctAnswers = models.IntegerField(default=0)
    videosSeen = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.date = datetime.datetime.today()
        return super(Score, self).save(*args, **kwargs)


def __unicode__(self):
    return str(self.score)
