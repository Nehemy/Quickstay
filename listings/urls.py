from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('properties/', properties, name='properties'),
    path('property/<str:pk>/', propertyDetails, name='property-details'),
    path('create-property/', createProperty, name='property-create'),
    path('update-property/<str:pk>/', updateProperty, name='update-property'),
    path('delete-property/<str:pk>/', deleteProperty, name='delete-property'),
    path('account/enquiries/', HostEnquiryListView.as_view(), name='host-enquiries'),
]
