from django.shortcuts import render
from .camera import *
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

# Create your views here.
def home(request):
    return render(request, 'stream/home.html')

@gzip.gzip_page
def stream(request):
    try:
        cam = Camera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad!
        pass

def stream(request, *args, **kwargs):
    return render(request, 'stream/stream.html')