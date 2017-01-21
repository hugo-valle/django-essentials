from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader      # for you html/css templates
from .models import Album

# Create your views here.
def index(request):
    all_albums = Album.objects.all()    # connect to db and get all recs from table
    template = loader.get_template()
    #html = ""
    #for album in all_albums:
     #   url = '/music/' + str(album.id) + '/'
      #  html += "<a href='" + url + "'>" + album.album_title + "</a><br>"
    #return HttpResponse("<h1>This is the music app homepage</h1>")
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id: " + str(album_id) + "</h2>")

