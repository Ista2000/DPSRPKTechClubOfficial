# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


@login_required(login_url='/users/login')
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['sidebar'] = 'base_sidebar.html'
    else:
        context['sidebar'] = 'base_sidebar_visitor.html'
    return render(request, 'home.html', context)
