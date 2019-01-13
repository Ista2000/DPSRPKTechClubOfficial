from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUser(AbstractUser):
    DEPARTMENT_CHOICES = (('CP', 'Competitive Programming'), ('DEV', 'Development'), ('ROB', 'Robotics'))
    userclass = models.IntegerField(_('class'), default=11)
    usersection = models.CharField(max_length=1)
    phno = models.IntegerField(default=1234567890)
    dept1 = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    dept2 = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    cchandle = models.CharField(max_length=50)
    cfhandle = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    isdpsite = models.BooleanField(default=False)

    def __str__(self):
        return self.username + ':' + self.first_name + ' ' + self.last_name + ':' + str(self.userclass) \
               + self.usersection
