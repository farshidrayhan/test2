# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_drug_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(max_length=50)),
                ('fingerprint', models.CharField(max_length=900)),
            ],
        ),
        migrations.DeleteModel(
            name='drug_table',
        ),
    ]
