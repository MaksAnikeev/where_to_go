from django.core.management.base import BaseCommand
from ...models import Image, Place
import requests
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = u'Заполнение базы данных по ссылке на джейсон'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help=u'url адрес джейсона'
            )

    def download_images(self, place_params, title, place):
        imgs = place_params.get('imgs')
        for number, img in enumerate(imgs, start=1):
            response_img = requests.get(img)
            response_img.raise_for_status()
            content_file = ContentFile(response_img.content, name=f'{title}{number}.jpg')
            Image.objects.create(
                place=place,
                img=content_file,
                number=number,
            )

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        response = requests.get(url)
        response.raise_for_status()
        place_params = response.json()
        title = place_params.get('title')
        description_short = place_params.get('description_short')
        description_long = place_params.get('description_long')
        lng = place_params.get('coordinates')['lng']
        lat = place_params.get('coordinates')['lat']
        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'description_short': description_short,
                'description_long': description_long
                },
            lng=lng,
            lat=lat
            )

        if created:
            self.download_images(
                place_params=place_params,
                title=title,
                place=place)
            print(f'Объект {title} с соответствующими картинками создан')
