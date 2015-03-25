from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views, gameViews, scoreViews, resultViews, userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^play/$', views.play, name='play'),
    url(r'^submit_score/$', views.submit_score, name="submit_score"),
    url(r'^scores/$', scoreViews.scores, name = 'scores'),
    url(r'^results/$', resultViews.results, name = 'results'),
    url(r'^user/(?P<user_name>[\w\-]+)/$', userViews.userProfile,
        name = 'profile'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'), 
)
