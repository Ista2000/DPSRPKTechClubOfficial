from django.db import models
from users.models import CustomUser

# Create your models here.


class Pad(models.Model):
    users = models.ManyToManyField(CustomUser, related_name='users')
    hash = models.CharField(max_length=50)
