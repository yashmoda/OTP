# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('name', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('phone', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]
