# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('travel_date_from', models.DateTimeField()),
                ('travel_date_to', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buddy', models.ManyToManyField(related_name='travel_buddies', to='log_reg_app.User')),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_planner', to='log_reg_app.User')),
            ],
        ),
    ]
