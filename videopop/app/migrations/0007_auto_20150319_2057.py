# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_video_videoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='videoid',
            field=models.CharField(default=datetime.datetime(2015, 3, 19, 20, 57, 53, 72000, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(unique=True),
            preserve_default=True,
        ),
    ]
