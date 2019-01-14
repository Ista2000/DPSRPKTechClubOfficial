from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Blog(models.Model):
    code = models.CharField(_('blog code'), max_length=15, default='')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='user')
    title = models.CharField(_('title'), max_length=200)
    dateposted = models.DateField(_('date posted'), default=timezone.now())
    body = models.TextField(_('blog body'))
    displaypic = models.FileField(_('display image'), default='')
    isurgent = models.BooleanField(_('announcement'), default=False)

    def __str__(self):
        return self.title
