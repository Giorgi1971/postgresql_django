from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms.widgets import Input
from .models import Person
from django.forms import EmailField, CharField, IntegerField, DateInput, DateTimeInput


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['card_number', 'personal_number', 
        'first_name', 'last_name',
        'photo', 'sex',
        'issuing_authority', 'birth_date',
        'birth_place', 'citizen',
        ]
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'}),
            'first_name': Input(attrs={'placeholder': 'Enter Name'}),
            'last_name': Input(attrs={'placeholder': 'Enter Surname'}),
            'card_number': Input(attrs={'placeholder': 'Enter Card Number'}),
            'personal_number': Input(attrs={'placeholder': 'Enter Only Numbers'}),
        }

