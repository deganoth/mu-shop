# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-13 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_guitar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guitar',
        ),
    ]
