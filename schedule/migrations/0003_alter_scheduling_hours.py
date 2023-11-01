# Generated by Django 4.2.6 on 2023-11-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_scheduling_day_scheduling_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='hours',
            field=models.CharField(choices=[('1', '8:00'), ('2', '9:00'), ('3', '10:00'), ('4', '11:00'), ('5', '12:00'), ('6', '13:00'), ('7', '14:00'), ('8', '15:00'), ('9', '16:00'), ('10', '17:00'), ('11', '18:00'), ('12', '19:00'), ('13', '20:00')], default=1, max_length=10),
        ),
    ]