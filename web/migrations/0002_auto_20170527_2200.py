# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bar',
            old_name='balance',
            new_name='beer_cost',
        ),
    ]
