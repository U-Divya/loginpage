# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-11 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dateofdeath',
            field=models.DateField(blank=True, null=True),
        ),
    ]
