# Generated by Django 4.2.9 on 2024-01-10 07:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("navigation", "0003_alter_navigationsettings_primary_navigation"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NavigationSettings",
        ),
    ]
