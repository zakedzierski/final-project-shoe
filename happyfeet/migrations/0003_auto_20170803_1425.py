# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-03 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyfeet', '0002_myshoe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myshoe',
            name='brand',
            field=models.CharField(choices=[('Addidas', 'Addidas'), ('Nike', 'Nike'), ('New Balance', 'New Balance'), ('Asics', 'Asics'), ('Brooks', 'Brooks'), ('Under Armour', 'Under Armour')], default='addidas', max_length=30),
        ),
        migrations.AlterField(
            model_name='myshoe',
            name='icon',
            field=models.CharField(choices=[('Running Shoe', 'Running Shoe'), ('Running Spike', 'Running Spike'), ('Competition Running Shoe', 'Competition Running Shoe')], default='running_shoe.png', max_length=30),
        ),
    ]