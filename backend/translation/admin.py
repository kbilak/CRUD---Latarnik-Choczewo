from django.contrib import admin
from .models import *


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ['code', 'language', 'translation']
    list_filter = ['code', 'translation', 'language']
    list_editable = ['translation',]
    search_fields = ['code', 'translation']

    class Meta:
        model = Translation


class TranslationLanguageAdmin(admin.StackedInline):
    model = Translation
    extra = 1


class TranslationCodeAdmin(admin.StackedInline):
    model = Translation
    extra = 1


@admin.register(Code)
class KodAdmin(admin.ModelAdmin):
    list_display = ['code', 'number_of_languages']
    list_filter = ['code']
    search_fields = ['code']
    inlines = [TranslationCodeAdmin]

    def number_of_languages(self, obj):
        return obj.translation_set.count()
    
    number_of_languages.short_description = 'Number of languages'

    class Meta:
        model = Code


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'number', 'active', 'translations_count']
    list_filter = ['active']
    list_editable = ['active', 'number']
    search_fields = ['name']
    inlines = [TranslationLanguageAdmin]

    def translations_count(self, obj):
        return obj.translation_set.count()
    
    translations_count.short_description = 'Translations'

    class Meta:
        model = Language
        