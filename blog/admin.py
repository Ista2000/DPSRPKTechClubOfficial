from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'dateposted', 'body', 'displaypic', 'isurgent')
    list_display = ('code', 'user', 'title', 'dateposted', 'body', 'displaypic', 'isurgent')


admin.site.register(Blog, BlogAdmin)
