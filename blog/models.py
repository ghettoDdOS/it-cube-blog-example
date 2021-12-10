import datetime

from django.db import models


class News(models.Model):
    """Модель новости"""

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=255,
        null=True,
    )
    preview = models.ImageField(
        verbose_name="Изображение",
        upload_to="static/news-img/",
        null=True,
    )
    date_of_publication = models.DateTimeField(
        verbose_name="Дата публикации",
        default=datetime.datetime.now,
    )
    text = models.TextField(
        verbose_name="Текст",
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_of_publication"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
