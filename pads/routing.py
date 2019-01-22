from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/pad/(?P<pad_hash>[^/]+)/$', consumers.PadConsumer),
]