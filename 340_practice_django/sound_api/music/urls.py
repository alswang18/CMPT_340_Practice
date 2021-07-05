
from django.urls import path
from .views import SongList

urlpatterns = [
    path("api/courses/", SongList.as_view()),
]