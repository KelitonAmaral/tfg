# Generated by Django 3.1.5 on 2021-11-22 09:28

import django.contrib.auth.models
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('type', models.CharField(choices=[('ADMINISTRATOR', 'Administrator'), ('ATHLETE', 'Athlete'), ('COACH', 'Coach'), ('GUEST', 'Guest')], default='GUEST', help_text='* Required fields', max_length=13, verbose_name='User type *')),
                ('name', models.CharField(max_length=100, verbose_name='Name *')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='Email')),
                ('cpf', models.CharField(help_text='ATENTION: just numbers', max_length=14, verbose_name='CPF *')),
                ('phone', models.CharField(help_text='ATENTION: just numbers', max_length=14, verbose_name='Cellphone *')),
                ('birth_date', models.DateField(help_text='dd/mm/aaaa', verbose_name='Date of birth *')),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=10, verbose_name='Gender *')),
                ('is_active', models.BooleanField(default=False, help_text='If active, the user has permission to access the system', verbose_name='Active')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Weight (Kg)')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Height (meters)')),
                ('regulatory_agency_registration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Regulatory agency registration ')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['type', 'name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('administrators', users.models.AdministratorActiveManager()),
                ('athletes', users.models.AthleteActiveManager()),
                ('coaches', users.models.CoachActiveManager()),
                ('guests', users.models.GuestActiveManager()),
            ],
        ),
    ]
