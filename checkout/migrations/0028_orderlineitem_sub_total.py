# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-06 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0027_remove_orderlineitem_big_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='sub_total',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
