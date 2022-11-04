from django.db import models


class Place(models.Model):
  title = models.CharField(
    max_length=100,
    verbose_name='Название экскурсии'
  )
  description_short = models.TextField(
    verbose_name='Краткое описание'
  )

  description_long = models.TextField(
    verbose_name='Полное описание',
    blank=True,
  )

  lng = models.FloatField(
    verbose_name='Долгота/Longitude',
    blank=True,
    null=True)

  lat = models.FloatField(
    verbose_name='Широта/Latitude',
    blank=True,
    null=True)


  class Meta:
    db_table = 'place'
    verbose_name = 'место'

    verbose_name_plural = 'места'

  def __str__(self):
    return f'{self.title}'


class Image(models.Model):
  place = models.ForeignKey(Place,
                            on_delete=models.CASCADE,
                            verbose_name='Название экскурсии',
                            related_name='images')

  imgs = models.ImageField(
    upload_to='place_images',
    verbose_name='Картинки с экскурсии',
    blank=True,
  )

  number = models.IntegerField(
    verbose_name='Номер картинки',
    default=1,
    blank=True,
  )

  class Meta:
    db_table = 'image'
    verbose_name = 'картинка'

    verbose_name_plural = 'картинки'

  def __str__(self):
    return f'{self.number} {self.place}'

