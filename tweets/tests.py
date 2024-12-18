from django.test import TestCase
from django.contrib.auth.models import User
from.models import Tweet

# Create your tests here.
class TweetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.tweet = Tweet.objects.create(content='Test Tweet', user=self.user)

    def test_like_tweet(self):
        self.tweet.likes.add(self.user)
        self.assertEqual(self.tweet.total_likes(), 1)
