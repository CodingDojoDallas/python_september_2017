# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-25 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friended',
            field=models.ManyToManyField(related_name='_user_friended_+', to='login_registration_app.User'),
        ),
    ]
