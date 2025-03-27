from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from listings.models import *
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    
class PublicProfileView(DetailView):
    model = Profile
    template_name = 'accounts/public_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.object.user_type == 'host':
            context['properties'] = self.object.properties.all()
        else:
            context['properties'] = None
        return context

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.user_type == 'host':
            context['properties'] = self.object.properties.all()
        else:
            context['properties'] = None
        return context
    
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'accounts/account_form.html'
    fields = ['name', 'email', 'bio', 'profile_picture']
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user.profile