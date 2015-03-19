# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
    ]
