# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-16 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_drugs'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='name',
            field=models.CharField(default=0, max_length=900),
            preserve_default=False,
        ),
    ]
