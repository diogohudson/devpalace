from django.db import models

from devpalace.models import TimeStampedModel


class PartyType(TimeStampedModel):
    """This is the party type model, used to store the type of meetings with developers"""

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Meeting Type"
        verbose_name_plural = "Meeting Types"


class Party(TimeStampedModel):
    """This is the party model, used to store the meetings with developers"""

    name = models.CharField(max_length=100)
    happened_at = models.DateTimeField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    party_type = models.ForeignKey(
        PartyType,
        on_delete=models.CASCADE,
        related_name="party_party_type",
        null=False,
        blank=False,
    )
    status = models.CharField(
        max_length=100,
        default="waiting",
        choices=(
            ("waiting", "Waiting"),
            ("canceled", "Canceled"),
            ("completed", "Completed"),
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"


class PartyPrince(TimeStampedModel):
    """This is the party prince model, used to store the prince who attended the meetings"""

    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
        related_name="party_prince_party",
        null=True,
        blank=True,
    )
    prince = models.ForeignKey(
        "prince.Prince",
        on_delete=models.CASCADE,
        related_name="party_prince_prince",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    was_present = models.BooleanField(default=False)
    was_proactive = models.BooleanField(default=False)
    was_helpful = models.BooleanField(default=False)
    was_responsive = models.BooleanField(default=False)
    was_respectful = models.BooleanField(default=False)
    was_friendly = models.BooleanField(default=False)

    def __str__(self):
        return self.party.name

    class Meta:
        unique_together = ("party", "prince")
        ordering = ["party__name", "prince__user__username"]
        verbose_name = "Meeting Member"
        verbose_name_plural = "Meeting Members"
