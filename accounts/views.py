from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *

def index(request):
    HttpResponse("Test")

# class ProfileDetailView(DetailView):
#     model = Profile
    
    
