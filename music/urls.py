from django.conf.urls import url
from . import views


app_name = 'music'  # for namespace name tags


urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name="index"),      # open function views.index
    # /music/rec_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
]
