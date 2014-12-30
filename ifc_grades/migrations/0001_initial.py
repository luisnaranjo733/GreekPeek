# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0005_chapter_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeReport',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('quarter', models.CharField(max_length=10, choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Summer', 'Summer')])),
                ('year', models.IntegerField()),
                ('chapter', models.ForeignKey(to='chapters.Chapter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
