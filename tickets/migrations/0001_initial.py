# Generated by Django 5.1.1 on 2024-09-10 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
                'db_table': 'Guest',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=100)),
                ('movie', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': 'Movie',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_reservation', to='tickets.guest')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='novie_reservation', to='tickets.movie')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
                'db_table': 'Reservation',
            },
        ),
    ]
