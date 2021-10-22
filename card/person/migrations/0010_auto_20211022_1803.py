# Generated by Django 3.2.8 on 2021-10-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_alter_person_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=7),
        ),
    ]