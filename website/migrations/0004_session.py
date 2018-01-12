# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 15:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20171228_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(help_text='Session ID', max_length=3, verbose_name='Session ID')),
                ('session_date', models.DateField(default=django.utils.timezone.now, help_text='Date of the session', verbose_name='Date of the session')),
                ('session_start_time', models.TimeField(default=datetime.date.today, help_text='Starting time', verbose_name='Starting time')),
                ('session_end_time', models.TimeField(default=datetime.date.today, help_text='End time', verbose_name='End time')),
                ('session_place', models.CharField(help_text='Location', max_length=25, verbose_name='Location')),
                ('session_instructors', models.CharField(help_text='Instructor(s)', max_length=100, verbose_name='Instructors')),
            ],
            options={
                'verbose_name': 'Session scheduling',
                'verbose_name_plural': 'Session scheduling',
            },
        ),
    ]