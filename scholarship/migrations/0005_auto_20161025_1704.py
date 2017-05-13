# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0004_auto_20161025_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='country',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='deadline',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='info_url',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholaship_name',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='university',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='user_country',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
