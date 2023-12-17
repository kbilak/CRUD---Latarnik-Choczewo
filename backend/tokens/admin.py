from django.contrib import admin
from .models import *
from django.utils.timezone import localtime


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'display_created_at', 'display_end_date', 'active')
    list_filter = ('created_at', 'end_date', 'active')
    search_fields = ('token',)
    readonly_fields = ('display_created_at', 'display_end_date')

    def display_created_at(self, obj):
        return localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')

    def display_end_date(self, obj):
        return localtime(obj.end_date).strftime('%Y-%m-%d %H:%M:%S')

    display_created_at.short_description = 'Created At'
    display_end_date.short_description = 'End Date'

    def get_fieldsets(self, request, obj=None):
        if obj:
            return (
                (None, {
                    'fields': ('token', 'display_created_at', 'display_end_date', 'active'),
                }),
            )
        return super().get_fieldsets(request, obj)

    def changelist_view(self, request, extra_context=None):
        # Check all tokens and update their 'active' status
        tokens = Token.objects.all()
        current_time = timezone.now()
        for token in tokens:
            if token.end_date < current_time:
                token.active = False
                token.save()

        return super().changelist_view(request, extra_context=extra_context)
    