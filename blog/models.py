from django.db import models
from users.models import CustomUser
import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(_('author'), CustomUser)
    title = models.CharField(_('title'), max_length=200)
    dateposted = models.DateField(_('date posted'), default=datetime.date.today())
    body = models.TextField(_('blog body'))
    displaypic = models.FileField(_('display image'), default='')
    isurgent = models.BooleanField(_('announcement'), default=False)

    def __str__(self):
        return self.title
