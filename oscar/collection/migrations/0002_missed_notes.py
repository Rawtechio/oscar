# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missed',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]