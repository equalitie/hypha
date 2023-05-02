# Generated by Django 3.2.18 on 2023-05-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0072_pafapprovals_approved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.TextField(choices=[('draft', 'Draft'), ('waiting_for_approval', 'Waiting for Approval'), ('contracting', 'Contracting'), ('in_progress', 'In Progress'), ('closing', 'Closing'), ('complete', 'Complete')], default='draft'),
        ),
    ]
