# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-28 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200228_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='description',
            field=models.TextField(),
        ),
    ]
