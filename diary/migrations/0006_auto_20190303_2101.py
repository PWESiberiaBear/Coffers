# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-03 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20190303_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialog',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='回答'),
        ),
    ]
