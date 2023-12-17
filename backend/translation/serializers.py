from rest_framework import serializers
from .models import *


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('code',)


class TranslationSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='code.code')

    class Meta:
        model = Translation
        fields = ['code', 'translation']


class LanguageSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True, read_only=True, source='translation_set',)

    class Meta:
        model = Language
        fields = ['name', 'code', 'translations']

    def get_translations(self, obj):
        translations = Translation.objects.filter(language=obj, code__active=True)
        return [
            {
                'code': translation.code.code,
                'translation': translation.translation
            }
            for translation in translations
        ]
