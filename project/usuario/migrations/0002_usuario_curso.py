# Generated by Django 3.0.4 on 2020-10-02 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='curso',
            field=models.ForeignKey(blank=True, help_text='ATENÇÃO: Professor, deixe em branco este atributo.', null=True, on_delete=django.db.models.deletion.PROTECT, to='curso.Curso', verbose_name='Curso'),
        ),
    ]