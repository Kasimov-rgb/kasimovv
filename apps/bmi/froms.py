from django import forms
from apps.bmi.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'weight', 'height']
