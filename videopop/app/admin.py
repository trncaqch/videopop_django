from django.contrib import admin
from app.models import Video, Score

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'reports']

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['user','score','date']
    

admin.site.register(Video, VideoAdmin)
admin.site.register(Score, ScoreAdmin)
