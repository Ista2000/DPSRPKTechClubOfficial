from django.contrib import admin
from .models import Pad

# Register your models here.


class PadAdmin(admin.ModelAdmin):

    list_display = ['hash', ]


admin.site.register(Pad, PadAdmin)
