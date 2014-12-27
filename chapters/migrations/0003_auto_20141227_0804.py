# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0002_chapter_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='bio',
            new_name='description',
        ),
    ]
