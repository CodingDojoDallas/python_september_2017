# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_delete_storemanager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='department',
        ),
    ]
