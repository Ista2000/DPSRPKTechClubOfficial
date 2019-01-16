from django.shortcuts import render, get_object_or_404, redirect
from .models import Pad
import secrets

# Create your views here.


def view_pad(request, pad_hash):
    if request.user.is_authenticated:
        pad = Pad.objects.get(hash=pad_hash)
        pad.users.add(request.user)
        return render(request, 'pads/pad.html', {'pad_hash': pad_hash})
    else:
        redirect('google.com')


def new_pad(request):
    if request.user.is_authenticated:
        pad_hash = secrets.token_urlsafe(nbytes=32)
        new_Pad = Pad(hash=pad_hash)
        new_Pad.users.add(request.user)
        new_Pad.save()
        return render(request, 'pads/pad.html', {'pad_hash': pad_hash})
    else:
        redirect('google.com')
