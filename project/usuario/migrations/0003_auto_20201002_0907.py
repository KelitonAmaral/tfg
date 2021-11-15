# Generated by Django 3.0.4 on 2020-10-02 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_curso'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['curso', 'nome', 'matricula'], 'verbose_name': 'usuário', 'verbose_name_plural': 'usuários'},
        ),
        migrations.AlterUniqueTogether(
            name='usuario',
            unique_together={('email', 'matricula')},
        ),
    ]
