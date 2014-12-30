# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifc_grades', '0002_auto_20141230_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradereport',
            name='cumulative_gpa',
            field=models.DecimalField(decimal_places=2, default=4.0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gradereport',
            name='new_member_gpa',
            field=models.DecimalField(decimal_places=2, default=4.0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gradereport',
            name='students_on_deans_list',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gradereport',
            name='submitted_chapter_size',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
