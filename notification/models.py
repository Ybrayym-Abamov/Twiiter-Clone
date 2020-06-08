from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.utils import timezone


class Notification(models.Model):
    notified_at = models.DateTimeField(default=timezone.now)
    target_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    notified_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    tweet_visibility = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.target_user} - {self.notified_tweet}'
