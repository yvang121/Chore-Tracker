# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
        ('chore_app', '0007_auto_20160330_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemate',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='house.House'),
        ),
    ]
