from django.shortcuts import render, redirect
from .models import Album, Song
from music.forms import AlbumForm, ImageForm

# Create your views here.

def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})

def album_song_list(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'song': song})

def create_album(request):
    if request.method == 'POST':
        #if user is submitting the form
        form = AlbumForm(request.POST)
        #form is the filled out ("bound") form with user data
        if form.is_valid():
            #django checks if form is valid (filled out with no missing or mistyped data)
            album = form.save()
            #because it's a ModelForm, saving it will create an instance of Album in the database
            #only need commit=False if you are going to add additional data not on the form (like request.user)
            return redirect("home")
    else: 
        form = AlbumForm()
        #^^^if user is visiting a page with GET request, not submitting the form yet, render a blank
    return render(request, 'music/create_album.html', {'form': form})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #Get the current instance object to display in the template
            Album.image = form.instance
            return render(request, 'index.html', {'form': form, 'Album.image': Album.image})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})