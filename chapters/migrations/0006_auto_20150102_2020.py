# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0005_chapter_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='latitude',
            field=models.DecimalField(decimal_places=3, max_digits=8, default='47.663092'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='longitude',
            field=models.DecimalField(decimal_places=3, max_digits=8, default='-122.309499'),
            preserve_default=False,
        ),
    ]
