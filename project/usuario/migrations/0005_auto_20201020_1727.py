# Generated by Django 3.1.2 on 2020-10-20 20:27

import django.contrib.auth.models
from django.db import migrations
import usuario.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20201008_1843'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('administradores', usuario.models.AdministradorAtivoManager()),
                ('coordenadores', usuario.models.CoordenadorAtivoManager()),
                ('orientadores', usuario.models.OrientadorAtivoManager()),
                ('professores', usuario.models.ProfessorAtivoManager()),
                ('alunos', usuario.models.AlunoAtivoManager()),
                ('secretarias', usuario.models.SecretariaAtivoManager()),
            ],
        ),
    ]
