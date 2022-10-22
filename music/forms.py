from django import forms
from .models import Album, Image

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        #this is the bit that is spicy, you can add as many fields as you want
        fields = ['title', 'artist',]

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
