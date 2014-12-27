# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0003_auto_20141227_0804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='description',
            new_name='bio',
        ),
    ]
