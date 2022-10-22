# Generated by Django 4.1.2 on 2022-10-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_image_remove_album_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.image'),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
