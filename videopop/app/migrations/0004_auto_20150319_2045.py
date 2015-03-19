# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_video_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='videoid',
            field=models.CharField(default=b'', unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
