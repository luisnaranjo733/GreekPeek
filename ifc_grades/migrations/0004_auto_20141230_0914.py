# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ifc_grades', '0003_auto_20141230_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradereport',
            name='quarter',
        ),
        migrations.RemoveField(
            model_name='gradereport',
            name='year',
        ),
        migrations.AddField(
            model_name='gradereport',
            name='day_in_that_quarter',
            field=models.DateField(default=datetime.datetime(2014, 12, 30, 9, 14, 4, 484246, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
