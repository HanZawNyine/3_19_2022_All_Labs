from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse,HttpResponse
from .video_camera import VideoCamera, gen



@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        print("StreamObj -----------------> ",StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame"))
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'camera_app/home.html')

def gg(request):
    return HttpResponse("<h1>Hello</h1>")