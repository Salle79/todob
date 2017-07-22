# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
