from django.shortcuts import render, redirect
from .models import *
from .forms import *

def createproperty(request):
    form = PropertyForm()
    
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'listings/property_form.html', context)

def propertydetails(request, pk):
    properties = Property.objects.get(id=pk)
    context = {'property':properties}
    return render(request, 'listings/property_details.html', context)

def updateproperty(request, pk):
    property = Property.objects.get(id=pk)
    form = PropertyForm(instance=property)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'listings/property_form.html', context)