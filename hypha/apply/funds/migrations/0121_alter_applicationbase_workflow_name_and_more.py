# Generated by Django 4.2.16 on 2024-11-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("funds", "0120_applicationsubmission_public_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicationbase",
            name="workflow_name",
            field=models.CharField(
                choices=[
                    ("single", "Request"),
                    ("single_same", "Request with same time review"),
                    ("single_ext", "Request with external review"),
                    ("single_com", "Request with community review"),
                    ("double", "Concept & Proposal"),
                ],
                default="single",
                max_length=100,
                verbose_name="Workflow",
            ),
        ),
        migrations.AlterField(
            model_name="applicationsubmission",
            name="workflow_name",
            field=models.CharField(
                choices=[
                    ("single", "Request"),
                    ("single_same", "Request with same time review"),
                    ("single_ext", "Request with external review"),
                    ("single_com", "Request with community review"),
                    ("double", "Concept & Proposal"),
                ],
                default="single",
                max_length=100,
                verbose_name="Workflow",
            ),
        ),
        migrations.AlterField(
            model_name="labbase",
            name="workflow_name",
            field=models.CharField(
                choices=[
                    ("single", "Request"),
                    ("single_same", "Request with same time review"),
                    ("single_ext", "Request with external review"),
                    ("single_com", "Request with community review"),
                    ("double", "Concept & Proposal"),
                ],
                default="single",
                max_length=100,
                verbose_name="Workflow",
            ),
        ),
        migrations.AlterField(
            model_name="roundbase",
            name="workflow_name",
            field=models.CharField(
                choices=[
                    ("single", "Request"),
                    ("single_same", "Request with same time review"),
                    ("single_ext", "Request with external review"),
                    ("single_com", "Request with community review"),
                    ("double", "Concept & Proposal"),
                ],
                default="single",
                max_length=100,
                verbose_name="Workflow",
            ),
        ),
    ]