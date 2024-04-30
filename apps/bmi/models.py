from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=100,
    )
    weight = models.FloatField(help_text='Weight in kilograms')
    height = models.FloatField(help_text='Height in meters')

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def __str__(self):
        return self.name
