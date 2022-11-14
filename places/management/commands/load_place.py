from django.core.management.base import BaseCommand
from ...models import Image, Place
import requests
import os


class Command(BaseCommand):
    help = u'Заполнение базы данных по ссылке на джейсон'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help=u'url адрес джейсона'
            )

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        response = requests.get(url)
        response.raise_for_status()
        place_params = response.json()
        title = place_params['title']
        description_short = place_params['description_short']
        description_long = place_params['description_long']
        lng = place_params['coordinates']['lng']
        lat = place_params['coordinates']['lat']
        place = Place.objects.get_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            lng=lng,
            lat=lat
            )

        imgs = place_params['imgs']
        for number, img in enumerate(imgs, start=1):
            response_img = requests.get(img)
            response_img.raise_for_status()
            file_path = os.path.join('media', 'place_images', f'{title}{number}.jpg')
            with open(file_path, 'wb') as file:
                file.write(response_img.content)
            Image.objects.get_or_create(
                place=place[0],
                img=os.path.join('place_images', f'{title}{number}.jpg'),
                number=number,
                )
        print(f'Объект {title} с соответствующими картинками создан')
