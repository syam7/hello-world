# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000)),
                ('feedback_text', models.TextField()),
            ],
        ),
    ]