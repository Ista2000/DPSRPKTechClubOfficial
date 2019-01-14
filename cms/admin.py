from django.contrib import admin
from .models import Problem, Contest, Tags
# Register your models here.


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('code', 'contest', 'get_author', 'get_contest', 'timelimit', 'statement', 'get_tags')

    def get_author(self, obj):
        return obj.author.username

    def get_contest(self, obj):
        return obj.contest.code


class ContestAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'rank_type', 'get_registerers')


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Tags, TagsAdmin)
