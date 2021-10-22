# Generated by Django 3.2.8 on 2021-10-22 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_person_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_place',
            field=models.CharField(default='Tbilisi', max_length=120),
        ),
        migrations.AlterField(
            model_name='person',
            name='card_number',
            field=models.CharField(default='1FR112345', max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='citizen',
            field=models.CharField(default='GEORGIA', max_length=24),
        ),
        migrations.AlterField(
            model_name='person',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 22, 16, 31, 18, 930466)),
        ),
        migrations.AlterField(
            model_name='person',
            name='issuing_authority',
            field=models.CharField(default='MINISTRY OF JUSTICE', max_length=256),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='Surname', max_length=48),
        ),
    ]
