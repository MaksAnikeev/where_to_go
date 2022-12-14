from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название экскурсии'
        )

    description_short = models.TextField(
        verbose_name='Краткое описание',
        default='',
        blank=True
        )

    description_long = HTMLField(
        verbose_name='Полное описание',
        blank=True,
        default='',
        )

    lng = models.FloatField(
        verbose_name='Долгота/Longitude',
        )

    lat = models.FloatField(
        verbose_name='Широта/Latitude',
        )

    class Meta:
        ordering = ['id']
        db_table = 'place'
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Название экскурсии',
        related_name='images'
        )

    img = models.ImageField(
        upload_to='place_images',
        verbose_name='Картинка с экскурсии',
        )

    number = models.IntegerField(
        verbose_name='Номер картинки',
        default=1,
        blank=True,
        )

    class Meta:
        ordering = ['place']
        db_table = 'image'
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return f'{self.number} {self.place}'
