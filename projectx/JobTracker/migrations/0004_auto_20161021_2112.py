# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-22 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobTracker', '0003_friendstable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendstable',
            name='reltype',
            field=models.CharField(max_length=10),
        ),
    ]