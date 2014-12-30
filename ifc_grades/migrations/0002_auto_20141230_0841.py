# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifc_grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradereport',
            name='quarter',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Spring', 'Spring')], max_length=10),
            preserve_default=True,
        ),
    ]
