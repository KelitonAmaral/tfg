# Generated by Django 3.1.2 on 2020-11-25 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20201020_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['tipo', 'curso', 'nome', '-matricula'], 'verbose_name': 'usuário', 'verbose_name_plural': 'usuários'},
        ),
    ]