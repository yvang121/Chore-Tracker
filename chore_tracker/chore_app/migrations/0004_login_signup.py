# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chore_app', '0003_auto_20160326_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=120)),
                ('password2', models.CharField(max_length=120)),
            ],
        ),
    ]