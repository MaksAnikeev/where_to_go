# Куда пойти — Москва глазами Артёма

Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

[Демка сайта](https://devmanorg.github.io/where-to-go-frontend/).

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 4 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DB_NAME` — имя базы данных, например: 'db.sqlite3'
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Соберите все файлы статики в одном месте. Создайте в корневом каталоге папку `collected_static`
укажите в файле settings.py значение:
```pycon
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = 'collected_static'
```

И запустите сервер с командой `collectstatic`
```
python manage.py collectstatic
```
После запуска верните значения в изначальное состояние:
```pycon
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'collected_static')]
STATIC_ROOT = ''
```
Запустите разработческий сервер

```
python3 manage.py runserver
```

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.


## Занесение данных через панель администратора

Чтобы использовать админ панель создайте суперпользователя

```
python3 manage.py createsuperuser
```
Панель администратора будет находится по адресу:

http://127.0.0.1:8000/admin/

Текущее имя - `user`, пароль - `user`

## Занесение данных через команду `load_place`

Данные с координатами, картинками и описанием также можно занести
через командную строку. Для этого необходимо вызвать команду
`load_place` с аргументом `путь до файла json` из корнегово каталога проекта:

```
python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%94%D0%BE%D0%BC%2C%20%D0%B3%D0%B4%D0%B5%20%D1%81%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%81%D1%8F%20%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%20%C2%AB%D0%9F%D0%BE%D0%BA%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%B0%C2%BB.json
```
Json файл должен иметь следующий вид:

```pycon
{
    "title": "Заброшенный пионерский лагерь «Белое озеро»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/631d8943c106ce547e65b00bb3b6d2fe.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/74d6828e96a20d9e4ce0d9e950a435c5.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/40df31b24bff7d2e0e82f3d8e1de0fae.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7144ffb1eea003cebacc05868ec917ab.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/2405ba96d7485ca581da6471ba1c93a4.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/139d8a217e4d5f1834f608ed5697457f.jpg"
    ],
    "description_short": "Пользовавшийся в советские годы большой популярностью летний лагерь  «Белое озеро» расположен около озера  с одноимённым названием. Как и все заброшенные места, этот лагерь привлекает своей умиротворённой атмосферой и любопытными находками, которые можно обнаружить, гуляя по территории.",
    "description_long": "<p>На берегу Белого озера, которое расположено неподалёку от платформы Белоозёрская, находится заброшенный пионерский лагерь. После распада Советского Союза окна и двери в лагере были заколочены, как и во многих государственных учреждениях. Несмотря на срок давности, здания и детские аттракционы  до сих пор стоят на прежнем месте и даже выглядят на редкость опрятными, словно делая вызов прошедшим годам.</p><p>Если вы решите съездить на разведку, то увидите, что пионерский лагерь опоясывает дорожка, гуляя по которой можно наткнуться на сцену Летнего театра, место для пионерской линейки, по левому краю  — на Столовую, по правому — на Живой уголок, а на дальнем краю лагеря — на Стадион и Клуб. Также на территории  есть небольшой питьевой фонтанчик, качели  и беседки.</p><p>После экскурсии по лагерю вы можете поплавать в озере (кстати, на его берегу стоят кабинки, где можно переодеться) и собрать землянику на его дальней стороне.</p>",
    "coordinates": {
        "lng": "38.24199999999999",
        "lat": "56.30184799999994"
    }
}
```

Подобные json файлы с описанием разных мест можно найти:

https://github.com/devmanorg/where-to-go-places/tree/master/places

Для использования ссылок на json необходимо выбрать локацию из списка, зайти в нее и нажать `Raw` - так вы получите адрес страницы, который необходимо использовать в команде `load_place`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

