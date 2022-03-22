from django.urls import path
from .views import Home,gg

urlpatterns = [
    path('gg/', Home),
    path('',gg)
]
