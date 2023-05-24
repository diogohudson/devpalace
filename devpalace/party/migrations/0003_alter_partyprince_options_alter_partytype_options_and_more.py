# Generated by Django 4.2.1 on 2023-05-24 20:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prince", "0004_alter_prince_options_alter_princeprincenote_options_and_more"),
        ("party", "0002_partyprince_was_friendly_partyprince_was_helpful_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="partyprince",
            options={
                "ordering": ["party__name", "prince__user__username"],
                "verbose_name": "Meeting Member",
                "verbose_name_plural": "Meeting Members",
            },
        ),
        migrations.AlterModelOptions(
            name="partytype",
            options={
                "ordering": ["name"],
                "verbose_name": "Meeting Type",
                "verbose_name_plural": "Meeting Types",
            },
        ),
        migrations.AlterUniqueTogether(
            name="partyprince",
            unique_together={("party", "prince")},
        ),
    ]