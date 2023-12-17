from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
import random, string


class Token(models.Model):
    token = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(64)

        if not self.end_date:
            self.end_date = self.created_at + timezone.timedelta(seconds=5)

        if self.end_date < timezone.now():
            self.active = False

        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' %(self.token)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Token'
        verbose_name_plural = 'Tokeny'
        