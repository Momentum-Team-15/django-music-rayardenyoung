from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        #this is the bit that is spicy, you can add as many fields as you want
        fields = ['title', 'artist',]