# Generated by Django 2.0.9 on 2019-03-07 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("funds", "0056_reviewers_rename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roundbase",
            name="start_date",
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
