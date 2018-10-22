# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-22 04:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighborHood',
            fields=[
                ('name', models.TextField(blank=True, max_length=50)),
                ('location', models.TextField(max_length=50, null=True)),
                ('occupants', models.TextField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Profile_photo', models.ImageField(blank=True, upload_to='images/')),
                ('Bio', models.TextField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_address', models.TextField(max_length=50, null=True)),
                ('neighbourhood', models.ManyToManyField(max_length=30, related_name='neighborhood', to='watch.NeighborHood')),
            ],
        ),
    ]