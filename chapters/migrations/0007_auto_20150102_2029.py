# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0006_auto_20150102_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7),
            preserve_default=True,
        ),
    ]
