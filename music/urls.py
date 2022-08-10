from django.urls import path
from .views import MusicListView, MusicDetailView

urlpatterns = [
    path('', MusicListView.as_view(), name='music_list'),
    path('<int:pk>/', MusicDetailView.as_view(), name='music_detail'),
]