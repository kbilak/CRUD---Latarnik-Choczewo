# Generated by Django 4.2.7 on 2023-12-17 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=1024)),
            ],
            options={
                'verbose_name': 'Code',
                'verbose_name_plural': 'Codes',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('code', models.CharField(default='', max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation', models.CharField(blank=True, default='', max_length=1024, null=True)),
                ('code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='translation.code')),
                ('language', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='translation.language')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
                'ordering': ('code', 'language'),
            },
        ),
    ]
