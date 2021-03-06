# Generated by Django 2.2.1 on 2020-08-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('registro', models.TextField(max_length=2000, verbose_name='Registro')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.MateriaModel')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]
