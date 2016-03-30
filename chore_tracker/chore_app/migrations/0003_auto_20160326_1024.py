# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('chore_app', '0002_housemate_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chore',
            options={'ordering': ['due_date']},
        ),
        migrations.AlterModelManagers(
            name='chore',
            managers=[
                ('chore_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='chore',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chore_app.Housemate', verbose_name='housemate responsible for completing this chore'),
        ),
        migrations.AlterField(
            model_name='housemate',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='housemate',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
    ]
