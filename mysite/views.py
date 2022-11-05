from django.shortcuts import render
from places.models import Place, Image
import os
import json
from pathlib import Path


def place_info(number, place):
    details(place, number)
    return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
             },
            "properties": {
                "title": place.title.partition('«')[2].partition('»')[0],
                "placeId": number,
                "detailsUrl": f"static/places/{number}.json"
                },
            }


def details(place, number):
    place_info = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
      }
    }
    directory_path = os.path.join('static', 'places')
    Path(directory_path).mkdir(parents=True,
                               exist_ok=True)
    file_path = os.path.join('static', 'places', f'{number}.json')
    with open(file_path, 'w', encoding='utf8') as json_file:
        json.dump(place_info, json_file, ensure_ascii=False)
    return number


def index_page(request):
    places = Place.objects.prefetch_related('images')
    context = {
        "places_info": {
            "type": "FeatureCollection",
            "features": [place_info(number, place) for number,place in enumerate(places)]}

    }
    return render(request, 'index.html', context)
