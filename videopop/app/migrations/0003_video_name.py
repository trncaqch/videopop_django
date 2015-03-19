# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150319_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 3, 19, 17, 34, 33, 509000, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
