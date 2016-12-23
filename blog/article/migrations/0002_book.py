# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=128, unique=True)),
                ('author', models.TextField()),
                ('publisher', models.TextField()),
                ('publicationdate', models.TextField()),
                ('printversion', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
    ]
