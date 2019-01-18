from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    DEPARTMENT_CHOICES = (('CP', 'Competitive Programming'), ('DEV', 'Development'), ('ROB', 'Robotics'))
    userclass = models.IntegerField(_('class'), default=11)
    usersection = models.CharField(_('section'), max_length=1)
    phno = models.CharField(_('ph. no.'), max_length=10)
    dept1 = models.CharField(_('first preference of department'), max_length=3, choices=DEPARTMENT_CHOICES)
    dept2 = models.CharField(_('second preference of department'), max_length=3, choices=DEPARTMENT_CHOICES)
    cchandle = models.CharField(_('codechef handle'), max_length=50, default='', blank=True)
    cfhandle = models.CharField(_('codeforces handle'), max_length=50, default='', blank=True)
    kagglehandle = models.CharField(_('kaggle handle'), max_length=50, default='', blank=True)
    rating = models.IntegerField(_('rating'), default=0)
    isdpsite = models.BooleanField(_('from dps'), default=False)
    profilepic = models.FileField(_('display image'), default='')
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=20)
    middle_name = models.CharField(_('middle name'), max_length=20, blank=True)
    last_name = models.CharField(_('last name'), max_length=20)

    def __str__(self):
        return self.username + ':' + self.first_name + ' ' + self.last_name + ':' + str(self.userclass) \
               + self.usersection
