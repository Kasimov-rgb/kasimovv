from django.contrib import admin
from apps.bmi.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'height', 'calculate_bmi')
    search_fields = ['name']
    list_filter = ['weight', 'height']

    def calculate_bmi(self, obj):
        return obj.calculate_bmi()

    calculate_bmi.short_description = 'BMI'
