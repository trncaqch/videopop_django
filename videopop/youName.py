import urllib
import simplejson

def getVideoName(video):
    id = video
    url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % id

    info = simplejson.load(urllib.urlopen(url))

    title = info['entry']['title']['$t']
    #author = info['entry']['author'][0]['name']

    return title
    #print "id:%s\nauthor:%s\ntitle:%s" % (id, author, title)
