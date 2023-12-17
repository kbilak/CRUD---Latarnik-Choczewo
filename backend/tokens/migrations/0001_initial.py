# Generated by Django 4.2.7 on 2023-12-17 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=6)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=128)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Kod',
                'verbose_name_plural': 'Kody',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokeny',
                'ordering': ('-created_at',),
            },
        ),
    ]