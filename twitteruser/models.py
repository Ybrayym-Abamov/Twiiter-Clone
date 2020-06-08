from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class TwitterUser(AbstractUser):
    displayname = models.CharField(max_length=30)
    joined_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
