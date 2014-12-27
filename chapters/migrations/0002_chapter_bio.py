# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='bio',
            field=models.TextField(default='Template bio text'),
            preserve_default=False,
        ),
    ]
