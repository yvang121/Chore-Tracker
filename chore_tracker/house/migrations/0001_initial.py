# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
            ],
            managers=[
                ('house_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]