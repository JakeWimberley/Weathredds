# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160714_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('events', models.ManyToManyField(blank=True, to='tracker.Event')),
            ],
        ),
    ]