# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150319_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videoid',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
