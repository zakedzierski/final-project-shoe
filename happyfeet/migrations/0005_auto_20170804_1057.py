# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyfeet', '0004_myshoe_shoe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myshoe',
            name='id',
        ),
        migrations.AlterField(
            model_name='myshoe',
            name='shoe_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
