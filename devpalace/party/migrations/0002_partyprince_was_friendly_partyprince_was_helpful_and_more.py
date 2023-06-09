# Generated by Django 4.2.1 on 2023-05-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("party", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="partyprince",
            name="was_friendly",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="partyprince",
            name="was_helpful",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="partyprince",
            name="was_present",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="partyprince",
            name="was_proactive",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="partyprince",
            name="was_respectful",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="partyprince",
            name="was_responsive",
            field=models.BooleanField(default=False),
        ),
    ]
