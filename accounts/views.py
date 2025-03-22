from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *

def index(request):
    return render(request, 'index.html')

# class ProfileDetailView(DetailView):
#     model = Profile
    
    
