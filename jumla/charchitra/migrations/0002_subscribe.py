# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('charchitra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pack', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subscription_time', models.DateTimeField(verbose_name='date published')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charchitra.Duration')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charchitra.VideoPackPrice')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charchitra.Video')),
            ],
        ),
    ]
