import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videopop.settings')

import django
django.setup()

import youParse
from app.models import Video

def populate():
    videosList = youParse.crawl(
        "www.youtube.com/watch?v=OPf0YbXqDm0&list=PL7C00E83736FB02C3")
    
    for s in videoList:
        print s
        add_video(s)

    for v in Video.objects.all():
        print v
    
    
def add_video(url):
    v = Video.objects.get_or_create(url = url)[0]
    return v

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()    
