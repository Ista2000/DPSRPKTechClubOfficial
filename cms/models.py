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
    registered_users = models.ManyToManyField(_('users registered'), CustomUser)
    rank_type = models.CharField(_('ranking type'), max_length=4, choices=RANK_TYPE)

    def __str__(self):
        return str(self.pk) + ":" + str(self.name)


class Problem(models.Model):
    contest = models.ForeignKey(_('contest'), Contest, on_delete=models.CASCADE)
    tags = models.ManyToManyField(_('tags'), Tags)
    userssolved = models.ManyToManyField(_('solved by'), CustomUser)
    author = models.ForeignKey(_('author'), CustomUser)
    solved = models.IntegerField(_('solved by'), default=0)
    solved_global = models.IntegerField(_('solved by(globally)'), default=0)
    code = models.CharField(_('problem code'), default=0)
    timelimit = models.IntegerField(_('time limit'), default=1)
    statement = models.FileField(_('problem statement'), default='')
    score = models.IntegerField(_('maximum score'), default=100)

    def __str__(self):
        return self.code


class Testcase(models.Model):
    inpfile = models.FileField(_('input file'), default='')
    outfile = models.FileField(_('output file'), default='')
    problem = models.ForeignKey(_('problem'), Problem, on_delete=models.CASCADE)

    def __str__(self):
        return "Test case for " + str(self.problem)


class Submission(models.Model):
    LANG_CHOICES = (('C', 'C'), ('CPP', 'C++'), ('PY', 'Python'), ('J', 'Java'))

    user = models.ForeignKey(_('by'), User, on_delete=models.CASCADE)
    problem = models.ForeignKey(_('problem'), Problem, on_delete=models.CASCADE)
    src = models.FileField(_('source code'), default='')
    lang = models.CharField(_('language'), max_length=3, choices=LANG_CHOICES)

    def __str__(self):
        return "Submission by " + str(self.user) + " for " + str(self.problem)
