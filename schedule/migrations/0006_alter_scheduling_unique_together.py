# Generated by Django 4.2.6 on 2023-11-07 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_alter_scheduling_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scheduling',
            unique_together={('collaborator', 'hours', 'day')},
        ),
    ]
