from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.CharField(max_length=6)
    username = models.CharField(max_length=128)
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username


class ChatHistory(models.Model):
    sender = models.CharField(max_length=128)
    receiver = models.CharField(max_length=128)
    message = models.CharField(max_length=255)
    timeStamp = models.TimeField(default=datetime.now)
    is_sent = models.BooleanField(default=True)

    def __str__(self):
        return (self.sender + " to " + self.receiver)

# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/


class UserConnection(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    userconnected = models.CharField(max_length=128)
    is_started = models.BooleanField(default=False)
    userid = models.CharField(max_length=6)
    connectionid = models.CharField(max_length=6)

    def __str__(self):
        return self.user.username


class connection(models.Model):
    name = models.CharField(max_length=128)
    profile_photo = models.CharField(max_length=512)
    password = models.CharField(max_length=16, default='123')
    is_started = models.BooleanField(default=False)

    def __str__(self):
        return self.name
