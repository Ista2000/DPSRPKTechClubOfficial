from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.SignUp.as_view(), name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
