from django.conf.urls import url
from . import views


app_name = 'music'  # for namespace name tags


urlpatterns = [
    # /music/
    url(r'^$', views.index, name="index"),      # open function views.index

    # /music/rec_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]
