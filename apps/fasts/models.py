from django.db import models

from apps.tags.models import Tag

from django.contrib.auth import get_user_model

User = get_user_model()


class Fast(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="fast/",
        verbose_name="Фото",
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="fast",
    )

    def __str__(self):
        return f"{self.title}"


class Images(models.Model):
    image = models.ImageField(
        upload_to="images/",
    )
    post = models.ForeignKey(
        Fast,
        on_delete=models.CASCADE,
        related_name="images",
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
