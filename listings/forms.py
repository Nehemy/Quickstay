from django.forms import ModelForm
from .models import *

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['description', 'address', 'city', 'state', 'country', 'price', 'property_type', 'amenities', 'cover_image']

class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'message']