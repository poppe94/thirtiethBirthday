# Generated by Django 5.0.1 on 2024-02-01 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overnight_stay', models.BooleanField(default=False)),
                ('food_preferences', models.CharField(choices=[('', 'Keine'), ('vegetarian', 'Vegetarisch'), ('vegan', 'Vegan')], default=('', 'Keine'), max_length=64)),
                ('display_name', models.CharField(blank=True, max_length=128)),
                ('link_identifier', models.CharField(max_length=128, unique=True)),
                ('visited', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gast',
                'verbose_name_plural': 'Gäste',
            },
        ),
        migrations.CreateModel(
            name='Entourage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overnight_stay', models.BooleanField(default=False)),
                ('food_preferences', models.CharField(choices=[('', 'Keine'), ('vegetarian', 'Vegetarisch'), ('vegan', 'Vegan')], default=('', 'Keine'), max_length=64)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invitation_manager.guest')),
            ],
            options={
                'verbose_name': 'Begleitung',
                'verbose_name_plural': 'Begleitung',
            },
        ),
    ]
