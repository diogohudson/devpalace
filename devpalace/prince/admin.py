from django.contrib import admin
from prince.models import Prince, PrincePrinceNote, PrinceRole


@admin.register(Prince)
class PrinceAdmin(admin.ModelAdmin):
    pass


@admin.register(PrinceRole)
class PrinceRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(PrincePrinceNote)
class PrincePrinceNoteAdmin(admin.ModelAdmin):
    pass
