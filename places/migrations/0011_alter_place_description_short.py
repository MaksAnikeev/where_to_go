# Generated by Django 4.1 on 2022-11-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_image_img_alter_place_lat_alter_place_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание'),
        ),
    ]