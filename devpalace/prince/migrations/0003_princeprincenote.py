# Generated by Django 4.2.1 on 2023-05-24 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("party", "0002_partyprince_was_friendly_partyprince_was_helpful_and_more"),
        ("prince", "0002_princerole_prince_is_active_prince_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrincePrinceNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("note", models.TextField()),
                ("require_feedback", models.BooleanField(default=False)),
                (
                    "created_from_party",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prince_prince_note_created_from_party",
                        to="party.party",
                    ),
                ),
                (
                    "prince",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prince_prince_note_prince",
                        to="prince.prince",
                    ),
                ),
                (
                    "prince_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prince_prince_note_prince_author",
                        to="prince.prince",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
