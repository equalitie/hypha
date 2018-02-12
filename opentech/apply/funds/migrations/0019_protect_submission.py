# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0018_add_addressfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationsubmission',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='applicationsubmission',
            name='round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='wagtailcore.Page'),
        ),
    ]
