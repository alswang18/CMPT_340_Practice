from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Song
from .serializers import SongSerializer

class SongList(APIView):
    def get(self, request, format=None):
        course = Song.objects.all()
        serializer = SongSerializer(course, many=True)
        return Response(serializer.data)
    

