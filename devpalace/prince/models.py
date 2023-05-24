from django.db import models

from devpalace.models import TimeStampedModel

# Create your models here.


class PrinceRole(TimeStampedModel):
    """This is the role of the prince"""

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Member Role"
        verbose_name_plural = "Member Roles"


class Prince(TimeStampedModel):
    """This is a one to one relationship with the User model"""

    user = models.OneToOneField(
        "auth.User",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="prince_created_by",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(
        PrinceRole,
        on_delete=models.CASCADE,
        related_name="prince_role",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["user__username"]
        verbose_name = "Member"
        verbose_name_plural = "Members"


class PrincePrinceNote(TimeStampedModel):
    prince_author = models.ForeignKey(
        Prince,
        on_delete=models.CASCADE,
        related_name="prince_prince_note_prince_author",
        null=False,
        blank=False,
    )
    prince = models.ForeignKey(
        Prince,
        on_delete=models.CASCADE,
        related_name="prince_prince_note_prince",
        null=False,
        blank=False,
    )
    note = models.TextField(null=False, blank=False)
    created_from_party = models.ForeignKey(
        "party.Party",
        on_delete=models.CASCADE,
        related_name="prince_prince_note_created_from_party",
        null=True,
        blank=True,
    )
    require_feedback = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.prince_author.user.username} - {self.prince.user.username} -"
            f" {self.note[:30]}"
        )

    class Meta:
        ordering = ["prince_author__user__username", "prince__user__username"]
        verbose_name = "Member Note"
        verbose_name_plural = "Member Notes"
