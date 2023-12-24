from django.contrib import admin
from .models import Player, Coach


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'status', 'number', 'year')
    search_fields = ('name',)
    list_filter = ('position', 'status', 'year',)
    readonly_fields = ('id',) 

    fieldsets = (
        (None, {
            'fields': ('id', 'name', 'position', 'status', 'image', 'number', 'year',)
        }),
    )


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'status', 'team')
    search_fields = ('name',)
    list_filter = ('type', 'status', 'team',)
    readonly_fields = ('id',) 

    fieldsets = (
        (None, {
            'fields': ('id', 'name', 'type', 'status', 'image', 'team',)
        }),
    )
    