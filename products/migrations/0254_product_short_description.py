# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0253_remove_product_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(default='', max_length=254),
        ),
    ]