# Generated by Django 4.1.2 on 2022-10-24 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_album_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='song',
        ),
    ]
