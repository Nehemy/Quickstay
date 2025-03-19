from django.shortcuts import render, request
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *

class ProfileDetailView(DetailView):
    model = Profile
    
    
