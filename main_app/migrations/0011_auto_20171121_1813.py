# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-21 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20171121_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_photo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='planet',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='planet',
            name='description_long',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='planet',
            name='small_photo',
            field=models.CharField(max_length=100),
        ),
    ]
