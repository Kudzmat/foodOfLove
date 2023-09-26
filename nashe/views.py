from django.shortcuts import render
from io import BytesIO
import base64
import os
from .functions import *
from urllib.parse import unquote


# Create your views here.
def nashe_albums(request):
    return render(request, "nashe/explore_tinashe.html")


def get_projects_cloud(request):
    banner_path = os.path.join('static', 'images', 'albums', 'nashe', '7.png')

    with open(banner_path, 'rb') as image_file:
        banner = base64.b64encode(image_file.read()).decode("utf-8")

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
        'banner': banner,
        'album': album
    }

    return render(request, 'nashe/word_cloud.html', context=context)


# getting word cloud for singular album
def get_album_cloud(request, encoded_album):
    # Decode the album name from the URL
    album = unquote(encoded_album)

    if album == "Songs For You":
        banner_path = os.path.join('static', 'images', 'albums', 'nashe', '10.png')

        with open(banner_path, 'rb') as image_file:
            banner = base64.b64encode(image_file.read()).decode("utf-8")

    elif album == '333':
        banner_path = os.path.join('static', 'images', 'albums', 'nashe', '9.png')

        with open(banner_path, 'rb') as image_file:
            banner = base64.b64encode(image_file.read()).decode("utf-8")

    elif album == 'BBANG3L':
        banner_path = os.path.join('static', 'images', 'albums', 'nashe', '8.png')

        with open(banner_path, 'rb') as image_file:
            banner = base64.b64encode(image_file.read()).decode("utf-8")

    else:
        banner_path = os.path.join('static', 'images', 'albums', 'nashe', '7.png')

        with open(banner_path, 'rb') as image_file:
            banner = base64.b64encode(image_file.read()).decode("utf-8")

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
        'album': album,
        'banner': banner
    }

    return render(request, 'nashe/word_cloud.html', context=context)
