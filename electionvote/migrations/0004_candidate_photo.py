# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electionvote', '0003_auto_20170313_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='photo',
            field=models.FileField(upload_to='candidates/', null=True, blank=True),
        ),
    ]