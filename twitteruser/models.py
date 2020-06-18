from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class TwitterUser(AbstractUser):
    displayname = models.CharField(max_length=30)
    joined_date = models.DateTimeField(default=timezone.now)
    following = models.ManyToManyField('self', symmetrical=False,
                                       related_name="following_someone")

    def __str__(self):
        return self.username
