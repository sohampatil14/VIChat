from django.db import models

# Create your models here.

class connection(models.Model):
    name = models.CharField(max_length=128)
    profile_photo = models.CharField(max_length=512)
    password = models.CharField(max_length=16, default='123')
    is_started = models.BooleanField(default=False)

    def __str__(self):
        return self.name
