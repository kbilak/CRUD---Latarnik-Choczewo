from rest_framework import serializers
from .models import Player, Coach


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'position', 'status', 'image', 'number', 'year',)


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'name', 'type', 'status', 'image', 'team',)
