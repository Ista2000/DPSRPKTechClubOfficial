# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/index.html', {})


@login_required(login_url='/users/login/')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
