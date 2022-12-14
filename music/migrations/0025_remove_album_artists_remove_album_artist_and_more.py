# Generated by Django 4.1.2 on 2022-10-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0024_remove_artist_albums_album_artists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artists',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(related_name='albums', to='music.artist'),
        ),
    ]
