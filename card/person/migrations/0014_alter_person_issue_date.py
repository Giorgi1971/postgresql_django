# Generated by Django 3.2.8 on 2021-10-22 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0013_alter_person_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='issue_date',
            field=models.DateField(default=datetime.date(2021, 10, 22)),
        ),
    ]