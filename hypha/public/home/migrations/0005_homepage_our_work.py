# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-20 13:36
from __future__ import unicode_literals

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_add_related_models_to_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="our_work",
            field=wagtail.fields.StreamField(
                (
                    (
                        "work",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StreamBlock(
                                (("title", wagtail.blocks.CharBlock()),)
                            )
                        ),
                    ),
                ),
                default=[],
            ),
            preserve_default=False,
        ),
    ]
