from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.new_pad, name='new_pad'),
    re_path(r'^(?P<pad_hash>[^/]+)/$', views.view_pad, name='view_pad'),
]
