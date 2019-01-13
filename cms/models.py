from django.db import models
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Tags(models.Model):
    name = models.CharField(_('name'), max_length=20, default='')

    def __str__(self):
        return self.name


class Contest(models.Model):
    RANK_TYPE = (('IOI', 'IOI'), ('ICPC', 'ICPC'), ('LONG', 'Long Challenge'), ('CF', 'Codeforces'))

    name = models.CharField(_('name'), max_length=50, default='')
    registered_users = models.ManyToManyField(CustomUser, related_name='registered_users')
    rank_type = models.CharField(_('ranking type'), max_length=4, choices=RANK_TYPE)

    def __str__(self):
        return str(self.pk)


class Problem(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='contest')
    tags = models.ManyToManyField(Tags, related_name='tags')
    userssolved = models.ManyToManyField(CustomUser, related_name='userssolved')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='author')
    solved = models.IntegerField(_('solved by'), default=0)
    solved_global = models.IntegerField(_('solved by(globally)'), default=0)
    code = models.CharField(_('problem code'), max_length=10)
    timelimit = models.IntegerField(_('time limit'), default=1)
    statement = models.FileField(_('problem statement'), default='')
    score = models.IntegerField(_('maximum score'), default=100)

    def __str__(self):
        return self.code


class Testcase(models.Model):
    inpfile = models.FileField(_('input file'), default='')
    outfile = models.FileField(_('output file'), default='')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='problem')

    def __str__(self):
        return self.pk


class Submission(models.Model):
    LANG_CHOICES = (('C', 'C'), ('CPP', 'C++'), ('PY', 'Python'), ('J', 'Java'))

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='submitted_by')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='for_problem')
    src = models.FileField(_('source code'), default='')
    lang = models.CharField(_('language'), max_length=3, choices=LANG_CHOICES)

    def __str__(self):
        return self.pk
