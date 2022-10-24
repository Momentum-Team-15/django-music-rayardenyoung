from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    

class Album(models.Model):
    title = models.CharField(max_length=200)
    # artist = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='images/')
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    # song = models.ManyToManyField('Song', related_name='albums')

    def __str__(self):
        return f"{self.title} by {self.artist}"
    

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ManyToManyField('Album', related_name='songs')

    def __str__(self):
        return f"{self.name}"
