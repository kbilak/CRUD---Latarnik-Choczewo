# Generated by Django 4.2.7 on 2023-12-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Rocznik'),
        ),
    ]
