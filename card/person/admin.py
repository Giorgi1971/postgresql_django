from django.contrib import admin
from .models import Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [
            'first_name', 'last_name', 'citizen', 'sex']}),

        ('Card information', {'fields': [
            'personal_number', 'card_number']}),

        ('Date information', {'fields': [
            'issue_date', 'expiry_date', 'issuing_authority', 'birth_date', 'birth_place']}),

        ('Upload photo', {'fields': [
            'photo']}),
    ]
    list_display = ('first_name', 'last_name', 'birth_date', 'personal_number')
    list_filter = ['last_name']
    search_fields = ['personal_number']


admin.site.register(Person, PersonAdmin)

