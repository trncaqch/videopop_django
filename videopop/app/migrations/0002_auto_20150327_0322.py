# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='reports',
            field=models.IntegerField(default=0, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0, max_length=128),
            preserve_default=True,
        ),
    ]
