from django.db import models
from django.contrib.auth import get_user_model

from django.utils.safestring import mark_safe

User = get_user_model()


class Trainer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Тренер",
    )
    specialization = models.CharField(
        max_length=100,
        verbose_name="Специализация",
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Зарплата",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'

# class Trainner(models.Model):
#     full_name = models.CharField(
#         max_length=100,
#         verbose_name="Название",
#     )
#     mobile = models.CharField(
#         max_length=100,
#         verbose_name="Телефон",
#     )
#     address = models.TextField()
#     is_active = models.BooleanField(default=False)
#     detail = models.TextField()
#     img = models.ImageField(upload_to="trainsers/")
#
#     def __str__(self):
#         return str(self.full_name)
#
#     def image_tag(self):
#         if self.img:
#             return mark_safe('<img scr="%s" width="80"/>' % self.img.url)
#         else:
#             return 'no-image'
