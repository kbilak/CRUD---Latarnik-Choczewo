from django.db import models
import uuid
from tokens.models import Token

class Player(models.Model):
    POSITION_CHOICES = [
        ('BR', 'Bramkarz'),
        ('OB', 'Obrońca'),
        ('PO', 'Pomocnik'),
        ('NA', 'Napastnik'),
    ]

    STATUS_CHOICES = [
        ('aktywny', 'Aktywny'),
        ('nieaktywny', 'Nieaktywny'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, verbose_name='Imię i nazwisko')
    position = models.CharField(max_length=2, choices=POSITION_CHOICES, verbose_name='Pozycja')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    image = models.ImageField(upload_to='players/', blank=True, null=True, verbose_name='Zdjęcie')
    number = models.IntegerField(verbose_name='Number', blank=True, null=True)
    year = models.CharField(max_length=4, verbose_name='Rocznik', blank=True, null=True)

    def __str__(self):
        return self.name


class Coach(models.Model):
    TYPE_CHOICES = [
        ('GW', 'Główny'),
        ('AS', 'Asystent')
    ]

    STATUS_CHOICES = [
        ('aktywny', 'Aktywny'),
        ('nieaktywny', 'Nieaktywny'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, verbose_name='Imię i nazwisko')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, verbose_name='Pozycja')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    image = models.ImageField(upload_to='players/', blank=True, null=True, verbose_name='Zdjęcie')
    team = models.CharField(max_length=4, verbose_name='Drużyna', blank=True, null=True)

    def __str__(self):
        return self.name
