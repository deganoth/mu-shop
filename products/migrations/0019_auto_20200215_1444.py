# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-15 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200215_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
    ]
