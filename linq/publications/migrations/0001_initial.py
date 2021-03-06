# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('comment_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Linq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_image', models.ImageField(upload_to=b'')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
