from django.shortcuts import render, get_object_or_404, redirect
import secrets
from django.contrib.auth.decorators import login_required
from django.http import Http404
from DPSRPKTechClub.settings import BASE_DIR

# Create your views here.


@login_required(login_url='/users/login/')
def view_pad(request, pad_hash):
    try:
        f = open(BASE_DIR+'\\pads\\padcontent\\'+pad_hash, "r")
    except FileNotFoundError:
        raise Http404
    return render(request, 'pads/pad.html', {'pad_hash': pad_hash, 'in_code': f.read()})


@login_required(login_url='/users/login/')
def new_pad(request):
    pad_hash = secrets.token_urlsafe(nbytes=64)
    pad_hash = pad_hash+".txt"
    f = open(BASE_DIR+'\\pads\\padcontent\\'+pad_hash, 'w+')
    string = 'function foo(items) {\n\tvar x = "All this is syntax highlighted";\n\treturn x;\n}'
    f.write(string)
    return redirect(str(pad_hash))
