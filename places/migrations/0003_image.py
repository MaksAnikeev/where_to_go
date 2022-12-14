# Generated by Django 4.1.2 on 2022-11-04 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20221104_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgs', models.ImageField(blank=True, upload_to='place_images', verbose_name='Картинки с экскурсии')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Название экскурсии')),
            ],
        ),
    ]
