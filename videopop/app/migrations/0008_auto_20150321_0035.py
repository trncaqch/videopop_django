# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150319_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='correctAnswers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='score',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 0, 35, 11, 484000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='videosSeen',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
