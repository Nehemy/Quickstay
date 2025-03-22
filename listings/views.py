from django.shortcuts import render
from .models import *
from .forms import *

def createproperty(request):
    form = PropertyForm()
    context = {'form':form}
    return render(request, 'listings/property_form.html', context)
