import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videopop.settings')

import django
django.setup()

from youName import getVideoName
from youParse import crawl
from app.models import Video


def populate():
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

if __name__ == '__main__':
    print 'Starting VideoPop population script...'
    populate()
