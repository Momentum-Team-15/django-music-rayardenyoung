from django.contrib import admin
from .models import User, Album, Artist, Song, Favorite

# Register your models here.
admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Favorite)