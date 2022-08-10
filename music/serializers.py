from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = ['id', 'owner', 'name', 'singer', 'review', 'created_at']
        fields = '__all__'