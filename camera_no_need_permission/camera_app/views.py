from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse,HttpResponse
from .video_camera import VideoCamera, gen



@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'camera_app/home.html')