# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chore_app', '0009_auto_20160404_0258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housemate',
            options={'ordering': ['last_name']},
        ),
    ]