import ast
import datetime
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    name = models.CharField(max_length=128)
    videoid = models.CharField(max_length=128)
    reports = models.IntegerField(max_length=128, default = 0)

class Score(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    score = models.IntegerField(max_length=128, default = 0)
    correctAnswers = models.IntegerField(default=0)
    videosSeen = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.date = datetime.datetime.today()
        return super(Score, self).save(*args, **kwargs)


def __unicode__(self):
    return str(self.score)
