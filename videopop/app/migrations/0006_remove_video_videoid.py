# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150319_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='videoid',
        ),
    ]
