# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chore_app', '0010_auto_20160406_0020'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
