# Generated by Django 2.1.11 on 2019-10-28 14:15

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import hypha.apply.projects.models


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0024_allow_no_comments_on_pr"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("public", models.BooleanField(default=True)),
                ("end_date", models.DateField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="application_projects.Project",
                    ),
                ),
            ],
            options={
                "ordering": ("-end_date",),
            },
        ),
        migrations.CreateModel(
            name="ReportConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("schedule_start", models.DateField(null=True)),
                ("occurrence", models.PositiveSmallIntegerField(default=1)),
                (
                    "frequency",
                    models.CharField(
                        choices=[("week", "Weeks"), ("month", "Months")],
                        default="month",
                        max_length=5,
                    ),
                ),
                (
                    "project",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="report_config",
                        to="application_projects.Project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportPrivateFiles",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "document",
                    models.FileField(
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to=hypha.apply.projects.models.report.report_path,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportVersion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("submitted", models.DateTimeField()),
                ("content", models.TextField()),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="application_projects.Report",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contract",
            name="approved_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="reportprivatefiles",
            name="report",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="files",
                to="application_projects.ReportVersion",
            ),
        ),
    ]
