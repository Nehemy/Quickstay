from django.urls import path
from .views import *

urlpatterns = [
    path('create-property/', createproperty, name='property-create'),
#     path('/properties', PropertyListView.as_view(), name='property-list'),
#     path('/<str:uuid>', PropertyDetailView.as_view(), name='property-detail'),
]
