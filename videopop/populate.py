import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videopop.settings')

import django
django.setup()

from app.models import Video

videoList = [{'id': 'wY-kAnvOY80', 'title' : 'Public Service Broadcasting - Gagarin'},
             {'id': '9bZkp7q19f0', 'title' : 'Psy - Gangnam Style'},
             {'id': '_u4Md_aXVJE', 'title' : 'Public Service Broadcasting - Spitfire'},
             {'id': 'WRu_-9MBpd4', 'title' : 'The Lonely Island - Great Day'}, 
             {'id' : 'ASO_zypdnsQ', 'title' : 'Psy - Gentleman'},
             {'id' : 'z5Otla5157c', 'title': 'The Lonely Island - YOLO'}]


def populate():
    for video in videoList:
        add_video(video['title'], video['id'])

        
    
def add_video(name, videoid):
    v = Video.objects.get_or_create(name = name)[0]
    v.videoid = videoid
    v.save()

if __name__ == '__main__':
    print 'Starting VideoPop population script...'
    populate()