# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-18 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20170216_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='idc',
            name='ip_range',
            field=models.CharField(max_length=30, null=True, verbose_name='IP\u8303\u56f4'),
        ),
    ]