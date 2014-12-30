# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0004_auto_20141227_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='nickName',
            field=models.CharField(max_length=50, default='default nickname'),
            preserve_default=False,
        ),
    ]
