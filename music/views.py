from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader      # for you html/css templates
from .models import Album

# Create your views here.
def index(request):
    all_albums = Album.objects.all()    # connect to db and get all recs from table
    template = loader.get_template("music/index.html")
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context, request))


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id: " + str(album_id) + "</h2>")

