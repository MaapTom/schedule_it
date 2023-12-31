# Generated by Django 4.2.6 on 2023-11-08 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_userprofile_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='cpf',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='endereco',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='estado_civil',
            field=models.CharField(choices=[('Casado', 'Casado'), ('Solteiro', 'Solteiro'), ('Outro', 'Outro')], default='Outro', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default='O', max_length=10, null=True),
        ),
    ]
