# Generated by Django 4.1.2 on 2022-11-06 15:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_remove_image_imgs_image_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['place'], 'verbose_name': 'картинка', 'verbose_name_plural': 'картинки'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['id'], 'verbose_name': 'место', 'verbose_name_plural': 'места'},
        ),
        migrations.AddField(
            model_name='place',
            name='description_long1',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
    ]