# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_flagged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(help_text='Day of the event in JJJJ-MM-DD', verbose_name='Day of the event (JJJJ-MM-DD)'),
        ),
    ]
