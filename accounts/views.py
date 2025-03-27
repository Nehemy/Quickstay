from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from listings.models import *

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile' : profile}
    return render(request, 'accounts/profile.html', context)

