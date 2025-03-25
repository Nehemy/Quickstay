from django.shortcuts import render, redirect
from .models import *
from .forms import *

def properties(request):
    properties = Property.objects.all()
    context = {'properties' : properties}
    return render(request, 'listings/properties.html', context)

def propertyDetails(request, pk):
    properties = Property.objects.get(id=pk)
    context = {'property':properties}
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