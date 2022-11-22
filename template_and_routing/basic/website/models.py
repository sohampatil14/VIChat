from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.CharField(max_length=6)
    status = models.CharField(max_length=128)

    # def __init__(self):
    # return self.user.username


class ChatHistory(models.Model):
    sender = models.CharField(max_length=128)
    receiver = models.CharField(max_length=128)
    message = models.CharField(max_length=255)
    timeStamp = models.TimeField(default=datetime.now)

# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
# class Connection(models.model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     connected = models.CharField(max_length=128)
#     is_started = models.BooleanField(default=False)


class connection(models.Model):
    name = models.CharField(max_length=128)
    profile_photo = models.CharField(max_length=512)
    password = models.CharField(max_length=16, default='123')
    is_started = models.BooleanField(default=False)

    def __str__(self):
        return self.name
