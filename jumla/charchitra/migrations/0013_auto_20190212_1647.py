# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charchitra', '0012_auto_20190212_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='videopackprice',
            name='duration',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='dur_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='videopackprice',
            name='dur_name',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Duration',
        ),
    ]
