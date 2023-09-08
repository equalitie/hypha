# Generated by Django 2.0.9 on 2019-02-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("activity", "0016_add_batch_ready"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("UPDATE_LEAD", "Update Lead"),
                    ("EDIT", "Edit"),
                    ("APPLICANT_EDIT", "Applicant Edit"),
                    ("NEW_SUBMISSION", "New Submission"),
                    ("SCREENING", "Screening"),
                    ("TRANSITION", "Transition"),
                    ("BATCH_TRANSITION", "Batch Transition"),
                    ("DETERMINATION_OUTCOME", "Determination Outcome"),
                    ("INVITED_TO_PROPOSAL", "Invited To Proposal"),
                    ("REVIEWERS_UPDATED", "Reviewers Updated"),
                    ("BATCH_REVIEWERS_UPDATED", "Batch Reviewers Updated"),
                    ("READY_FOR_REVIEW", "Ready For Review"),
                    ("BATCH_READY_FOR_REVIEW", "Batch Ready For Review"),
                    ("NEW_REVIEW", "New Review"),
                    ("COMMENT", "Comment"),
                    ("PROPOSAL_SUBMITTED", "Proposal Submitted"),
                    ("OPENED_SEALED", "Opened Sealed Submission"),
                    ("REVIEW_OPINION", "Review Opinion"),
                ],
                max_length=50,
            ),
        ),
    ]
