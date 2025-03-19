from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='home'),
    path('/<str:slug>', ProfileDetailView.as_view(), name='profile'),
]
