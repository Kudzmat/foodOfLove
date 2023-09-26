from django.urls import path
from . import views

app_name = 'nashe'

urlpatterns = [
    path("explore/", views.nashe_albums, name='nashe_albums'),
    path(f"word-cloud/<str:encoded_album>", views.get_album_cloud, name='get_album_cloud'),
    path("all-projects-cloud/All-Projects", views.get_projects_cloud, name='get_projects_cloud')
]
