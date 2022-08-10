from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Song
from .serializers import SongSerializer


# Create your views here.
class MusicListView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class MusicDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer