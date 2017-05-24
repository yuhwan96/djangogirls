# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('phone_no', models.CharField(max_length=11)),
                ('birthday', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='blog.User'),
        ),
    ]
