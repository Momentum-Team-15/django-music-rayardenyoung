# Generated by Django 4.1.2 on 2022-10-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_remove_album_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist_compendium',
            field=models.ManyToManyField(related_name='albums', to='music.artist'),
        ),
    ]