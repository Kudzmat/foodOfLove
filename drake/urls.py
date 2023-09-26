from django.urls import path
from . import views

app_name = 'drake'

urlpatterns = [
    path("explore/", views.search_drake, name='search_drake'),
    path(f"word-cloud/<str:encoded_album>", views.get_album_cloud, name='get_album_cloud'),
]