# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
                ('state', models.IntegerField()),
            ],
        ),
    ]