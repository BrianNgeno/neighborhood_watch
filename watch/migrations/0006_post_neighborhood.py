# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0005_auto_20181023_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighborHood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='watch.NeighborHood'),
        ),
    ]
