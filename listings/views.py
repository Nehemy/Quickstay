from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')

def properties(request):
    properties = Property.objects.all()
    context = {'properties' : properties}
    return render(request, 'listings/properties.html', context)

def propertyDetails(request, pk):
    property_obj = Property.objects.get(id=pk)
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.property = property_obj
            enquiry.save()
            messages.success(request, "Your enquiry has been submitted.")
            return redirect('property-details', pk=pk)
    else:
        form = EnquiryForm()
    
    context = {
        'property': property_obj,
        'enquiry_form': form,
    }
    return render(request, 'listings/property_details.html', context)

def createProperty(request):
    form = PropertyForm()
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('properties')
        
    context = {'form':form}
    return render(request, 'listings/property_form.html', context)


def updateProperty(request, pk):
    property = Property.objects.get(id=pk)
    form = PropertyForm(instance=property)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('properties')
        
    context = {'form':form}
    return render(request, 'listings/property_form.html', context)

def deleteProperty(request, pk):
    property = Property.objects.get(id=pk)
    if request.method =='POST':
        property.delete()
        return redirect('properties')
    
    context = {'object': property}
    return render(request, 'listings/confirm_delete.html', context)

class HostEnquiryListView(LoginRequiredMixin, ListView):
    model = Enquiry
    template_name = 'listings/host_enquiries.html'
    context_object_name = 'enquiries'
    
    def get_queryset(self):
        profile = self.request.user.profile
        if profile.user_type != 'host':
            return Enquiry.objects.none()
        return Enquiry.objects.filter(property__host=profile)