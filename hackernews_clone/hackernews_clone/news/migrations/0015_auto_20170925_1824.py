# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170925_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_time']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.News'),
            preserve_default=False,
        ),
    ]