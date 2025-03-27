from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from listings.models import *
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile' : profile}
    return render(request, 'accounts/profile.html', context)

