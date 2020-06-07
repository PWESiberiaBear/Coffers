# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-06-07 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XuexiRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5b8c\u6210')),
                ('record_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u7b7e\u5230\u65f6\u95f4')),
            ],
        ),
    ]
