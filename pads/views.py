from django.shortcuts import render, get_object_or_404

# Create your views here.


def view_pad(request, pad_hash):
    return render(request, 'pads/pad.html', {'pad_hash': pad_hash})


def new_pad(request):
    pad_hash = 'AAAA'
    return render(request, 'pads/pad.html', {'pad_hash': pad_hash})
