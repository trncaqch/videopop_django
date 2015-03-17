from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views, gameViews, scoreViews, resultViews, userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^play', gameViews.play, name='play'),
    url(r'^scores', scoreViews.scores, name = 'scores'),
    url(r'^results', resultViews.results, name = 'results'),
    url(r'^user/(?P<user_name>[\w\-]+)/$', userViews.userProfile,
        name = 'profile'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_ROOT)
