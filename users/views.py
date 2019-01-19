# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def home(request):
    context = {}
    if request.user.is_authenticated:
        context['sidebar'] = 'base_sidebar.html'
    else:
        context['sidebar'] = 'base_sidebar_visitor.html'
    return render(request, 'home.html', context)
