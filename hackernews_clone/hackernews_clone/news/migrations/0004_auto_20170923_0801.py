# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170921_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['rank']},
        ),
    ]