# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-12 17:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('prop1', models.CharField(max_length=100)),
                ('prop2', models.CharField(max_length=100)),
                ('prop3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('api_key', models.CharField(max_length=100)),
                ('api_secret', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
