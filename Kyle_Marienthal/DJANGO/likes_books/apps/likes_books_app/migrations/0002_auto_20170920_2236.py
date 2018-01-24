# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='liked_books',
        ),
        migrations.RemoveField(
            model_name='like',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(related_name='books', to='likes_books_app.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to='likes_books_app.User'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]