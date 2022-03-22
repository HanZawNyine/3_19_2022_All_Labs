from rest_framework.decorators import api_view

from rest_framework import status

from django.views.decorators import gzip
from django.http import StreamingHttpResponse,HttpResponse
from rest_framework.response import Response

from camera_app.video_camera import VideoCamera, gen



@gzip.gzip_page
@api_view(['GET',])
def home_api_view(request):
    try:
        cam = VideoCamera()
        print("---------------------->",StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame"))
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame",status=status.HTTP_200_OK)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
