from typing import Pattern
from django.db import models
from django.forms import widgets
from django.forms.fields import TimeField
from django.utils import timezone
from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError


# ვალიდატორი პირადი ნომერის გრაფაში მხოლოდ რიცხვების შეტანისათვის
def validate_numbers(value):
    if value.isnumeric():
        return value
    else:
        raise ValidationError("Must be only numbers!")


# პიროვნების მონაცემები, არაა User-ის შვილობილი, არც OneToOneField-ით დაკავშორებული
class Person(models.Model):
    card_number = models.CharField(max_length=9, unique=True)
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    photo = models.ImageField(upload_to='photo')
    citizen = models.CharField(max_length=24, default="GEORGIA")
    class SexType(models.TextChoices):
        M = 'Male', 'M' 
        F = 'Female', 'F' 
    sex = models.CharField(
        max_length=7,
        choices=SexType.choices,
    )
    personal_number = models.CharField(max_length=11, unique=True, validators=[validate_numbers])
    birth_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=120, default="Tbilisi")
    issue_date = models.DateField(default=date.today()) # პირობითად ჩავთვალე რომ პირადობის გაცემის დღეს ხდება მონაცემის შეტანა
    issuing_authority = models.CharField(max_length=256, default="MINISTRY OF JUSTICE")

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    # მეთოდი პირადობის ვადის დასრულების გრაფის ავტომატურად შესავსებად (+10 წელი)
    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = self.issue_date + timedelta(days=3652)
        super(Person, self).save(*args, **kwargs)