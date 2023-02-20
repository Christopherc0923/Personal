from django.shortcuts import render
import os
from django.conf import settings

# Create your views here.
def utube(request):
    path = os.path.join(settings.BASE_DIR, 'utube/static/utube')
    files = os.listdir(path)

    return render(request, 'utube/home.html', {'files': files})

from pytube import YouTube


def download_video(request):
    url = request.GET.get('url')
    yt = YouTube(url)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    video_filename = stream.default_filename
    file_path = os.path.join(settings.BASE_DIR, 'utube/static/utube', video_filename)
    stream.download(os.path.dirname(file_path))

    return render(request, 'utube/home.html', {'status': 'Video downloaded successfully'})

import urllib.parse

def show_video(request, video_title):
    video_title = urllib.parse.unquote(video_title)
    video_path = os.path.join(settings.BASE_DIR, 'utube/static/utube/{}'.format(video_title))
    if os.path.isfile(video_path):
        return render(request, 'utube/show_video.html', {'video_title': video_title, 'video_path': video_path})