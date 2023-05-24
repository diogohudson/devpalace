from django.contrib import admin
from party.models import Party, PartyPrince, PartyType
from prince.models import PrincePrinceNote


class PrincePrinceNoteInline(admin.TabularInline):
    model = PrincePrinceNote
    extra = 0


class PartyPrinceInline(admin.TabularInline):
    model = PartyPrince
    extra = 0


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    inlines = [PartyPrinceInline, PrincePrinceNoteInline]
    list_display = ("name", "party_type", "happened_at", "status")
    list_filter = ("status", "happened_at", "party_type")
    search_fields = ("name", "party_type__name", "party_prince_party__prince__name")


@admin.register(PartyPrince)
class PartyPrinceAdmin(admin.ModelAdmin):
    pass


@admin.register(PartyType)
class PartyTypeAdmin(admin.ModelAdmin):
    pass
