from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Fast(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, #после удаления пользовтяля удалятса его блоги
        verbose_name="Пользователь",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Названия",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="fast/",
        verbose_name="Фото",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

