# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charchitra', '0003_auto_20190212_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoprice',
            name='dur_id',
        ),
        migrations.AddField(
            model_name='videoprice',
            name='dur_name',
            field=models.CharField(default='d', max_length=40, unique=True),
        ),
    ]