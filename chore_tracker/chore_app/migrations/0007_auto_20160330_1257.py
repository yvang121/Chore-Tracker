# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chore_app', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
