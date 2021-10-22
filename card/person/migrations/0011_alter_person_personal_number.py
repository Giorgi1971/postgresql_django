# Generated by Django 3.2.8 on 2021-10-22 14:29

from django.db import migrations, models
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_auto_20211022_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personal_number',
            field=models.CharField(max_length=11, unique=True, validators=[person.models.validate_numbers]),
        ),
    ]