# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=40)),
                ('u_pass', models.CharField(max_length=40)),
            ],
        ),
    ]
