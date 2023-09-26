from django.shortcuts import render, redirect
from io import BytesIO
import base64
import os
from .functions import *
from urllib.parse import unquote
from .forms import *


# Create your views here.

# Create your views here.
def search_drake(request):
    # setting banner image
    banner_path = os.path.join('static', 'images', 'albums', 'drake', '7.png')
    with open(banner_path, 'rb') as image_file:
        banner = base64.b64encode(image_file.read()).decode("utf-8")

    form = AlbumSearchForm()
    album = ""

    if request.method == 'POST':
        form = AlbumSearchForm(request.POST)
        if form.is_valid():
            album = form.cleaned_data['album_name'].title()
            return redirect('drake:get_album_cloud', encoded_album=album)

    context = {
        'form': form,
        'album': album
    }
    return render(request, "drake/drake_search.html", context=context)


def get_projects_cloud(request):

    album = 'All Projects'

    # get selected album's lyrics
    proj_Lyrics = get_project_lyrics()

    # clean up lyrics
    clean_lyrics = process_lyrics(proj_Lyrics)

    # get word count
    word_count = check_frequency(clean_lyrics)

    # create word cloud
    word_cloud = create_word_cloud(word_count)

    # Convert the word cloud image to bytes
    image_stream = BytesIO()
    word_cloud.to_image().save(image_stream, format="PNG")  # Save as PNG format (or the desired format)
    image_stream.seek(0)
    encoded_image = base64.b64encode(image_stream.read()).decode("utf-8")

    context = {
        'word_cloud': encoded_image,
        'album': album
    }

    return render(request, 'drake/projects_cloud.html', context=context)


# getting word cloud for singular album
def get_album_cloud(request, encoded_album):
    # Decode the album name from the URL
    album = unquote(encoded_album)

    # get selected album's lyrics
    album_Lyrics = get_album_lyrics(album)

    # clean up lyrics
    clean_lyrics = process_lyrics(album_Lyrics)

    # get word count
    word_count = check_frequency(clean_lyrics)

    # create word cloud
    word_cloud = create_word_cloud(word_count)

    # Convert the word cloud image to bytes
    image_stream = BytesIO()
    word_cloud.to_image().save(image_stream, format="PNG")  # Save as PNG format (or the desired format)
    image_stream.seek(0)
    encoded_image = base64.b64encode(image_stream.read()).decode("utf-8")

    context = {
        'word_cloud': encoded_image,
        'album': album
    }

    return render(request, 'drake/drake_cloud.html', context=context)
