from django.db import models
import uuid
from django.utils import timezone


class User(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('normal', 'Normal'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    email = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Data dołączenia')
    user_type = models.CharField(choices=USER_TYPES, max_length=255, default='individual', verbose_name='Typ użytkownika')

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'
