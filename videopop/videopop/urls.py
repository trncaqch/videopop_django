from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views, gameViews, scoreViews, resultViews, userViews


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^play', gameViews.play, name='play'),
    url(r'^scores', scoreViews.scores, name = 'scores'),
    url(r'^results', resultViews.results, name = 'results'),
    url(r'^user/(?P<user_name>[\w\-]+)/$', userViews.userProfile,
        name = 'profile')
)
