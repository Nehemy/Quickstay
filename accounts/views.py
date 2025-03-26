from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *

def profile(request):
    return render(request, 'accounts/profile.html')

