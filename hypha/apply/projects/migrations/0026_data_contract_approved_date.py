# Generated by Django 2.1.11 on 2019-10-29 03:54

from django.db import migrations
from django.db.models import F


def copy_submitted_date(apps, schema_editor):
    Contract = apps.get_model("application_projects", "Contract")
    Contract.objects.all().update(approved_at=F("created_at"))


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0025_add_report_models"),
    ]

    operations = [
        migrations.RunPython(copy_submitted_date),
    ]
