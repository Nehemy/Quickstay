from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('<str:slug>', ProfileDetailView.as_view(), name='profile'),
]
