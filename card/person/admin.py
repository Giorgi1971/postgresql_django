from django.contrib import admin
from .models import Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [
            'first_name', 'last_name']}),

        ('Date information', {'fields': [
            'issue_date', 'expiry_date', 'issuing_authority']}),

        ('Card information', {'fields': [
            'card_number', 'personal_number']}),

        ('photo information', {'fields': [
            'photo', 'sex']}),


        ('Date information', {'fields': [
            'birth_date', 'birth_place', 'citizen']}),
    ]
    list_display = ('first_name', 'last_name', 'birth_date', 'personal_number')
    list_filter = ['last_name']
    search_fields = ['personal_number']


admin.site.register(Person, PersonAdmin)

