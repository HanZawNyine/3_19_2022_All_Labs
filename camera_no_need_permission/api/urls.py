from django.urls import path
from .views import home_api_view

urlpatterns = [
    path('',home_api_view),
]