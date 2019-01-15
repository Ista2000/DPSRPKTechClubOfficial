from django.db import models
from users.models import CustomUser
from pads.models import Pad

# Create your models here.


class Teach(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField(CustomUser, related_name='students')
    live_url = models.CharField(max_length=50, default='')
    pads = models.ManyToManyField(Pad, related_name='pads')
