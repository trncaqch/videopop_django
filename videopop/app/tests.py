from django.test import TestCase
from models import Video, Score
from youName import getVideoName
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# files

# Create your tests here.

class videoTest(TestCase):
    def video_has_name(self):
        video = Video(name = getVideoName("W9IIU8AJHCw"), videoid = "W9IIU8AJHCw")
        self.asserEquals(video.name, "Peer Kusiv - Hoch Tief")

    def video_has_id(self):
        video = Video(name = "Peer Kusiv - Hoch Tief", videoid = "W9IIU8AJHCw")
        self.asserEquals(video.videoid, "W9IIU8AJHCw")

class userTest(TestCase):
    def test_user_has_a_name(self):
        user = User(username="hi", password="x")
        user.save()
        self.assertEquals(user.username, "hi")


    def test_user_has_a_password(self):
        user = User(username="hi", password="x")
        user.save()
        self.assertEquals(user.password, "x")

class IndexViewTests(TestCase):
    def test_index_view_with_no_scores(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['top_scores'], [])

    def test_index_view_with_score(self):
        add_user("name", "pass", "a@a.com")
        user = User.objects.get(username = "name")
        add_score(user, 10, 10, 10);

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        num_scores = len(response.context['top_scores'])
        self.assertEqual(num_scores , 1)

class HighscoreViewTests(TestCase):
    def test_highscore_view_with_no_scores(self):
        response = self.client.get(reverse('scores'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['scores'], [])

    def test_highscore_view_with_scores(self):
        add_user("name", "pass", "a@a.com")
        user = User.objects.get(username = "name")
        add_score(user, 10, 10, 10);

        response = self.client.get(reverse('scores'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        num_scores = len(response.context['scores'])
        self.assertEqual(num_scores , 1)

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