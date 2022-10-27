# Generated by Django 4.1.2 on 2022-10-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_album_artist_compendium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist_compendium',
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_compendium',
            field=models.ManyToManyField(related_name='artists', to='music.album'),
        ),
    ]