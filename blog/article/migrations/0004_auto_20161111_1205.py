# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='pubDate',
            field=models.DateField(),
        ),
    ]
