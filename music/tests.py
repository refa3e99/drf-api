from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Song


# Create your tests here.
class SongTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test', password='test1234')
        test_user.save()
        test_song = Song.objects.create(name='test', owner=test_user, singer='test', review='test')
        test_song.save()

    def test_song_model(self):
        song = Song.objects.get(pk=1)
        self.assertEqual(str(song.owner), 'test')
        self.assertEqual(str(song.name), 'test')
        self.assertEqual(str(song.singer), 'test')
        self.assertEqual(str(song.review), 'test')
