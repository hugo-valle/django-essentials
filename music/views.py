from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.
def index(request):
    """
    Get all Album ojbects and display them
    :param request: http request
    :return: render of /music/index.html page
    """
    all_albums = Album.objects.all()    # connect to db and get all recs from table
    context = { 'all_albums' : all_albums, }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    """
    Detail view for album information
    :param request: http request
    :param album_id: album_id or pk
    :return: render of music/detail.html page
    """
    album = get_object_or_404(Album, pk=album_id)   # replaces the try/except statement
    context = { 'album' : album, }
    return render(request, 'music/detail.html', context)


def favorite(request, album_id):
    """
    Select favorite songs
    :param request: http request
    :param album_id: album_id or pk
    :return: render of music/detail.html page
    """
    album = get_object_or_404(Album, pk=album_id)   # replaces the try/except statement
    context = { 'album' : album,}
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        context['error_message'] = "You did not select a valid song"
        return render(request, 'music/detail.html', context)
    else:
        # Update db
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', context)

