from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')

def properties(request):
    properties = Property.objects.all()
    context = {'properties' : properties}
    return render(request, 'listings/properties.html', context)

def propertyDetails(request, pk):
    property_obj = get_object_or_404(Property, id=pk)
    
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

@login_required
def createProperty(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.host = request.user.profile
            property_obj.save()
            
            images = request.FILES.getlist('images')
            for image in images:
                PropertyImage.objects.create(property=property_obj, image=image)
            
            return redirect('account')
    else:
        form = PropertyForm()
    context = {'form': form}
    return render(request, 'listings/property_form.html', context)

@login_required
def updateProperty(request, pk):
    property_obj = get_object_or_404(Property, id=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            
            images = request.FILES.getlist('images')
            for image in images:
                PropertyImage.objects.create(property=property_obj, image=image)
                
            return redirect('account')
    else:
        form = PropertyForm(instance=property_obj)
    context = {'form': form}
    return render(request, 'listings/property_form.html', context)

def deleteProperty(request, pk):
    property = Property.objects.get(id=pk)
    if request.method =='POST':
        property.delete()
        return redirect('account')
    
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