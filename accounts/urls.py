from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<str:pk>/', profile, name='profile'),
    path('register/', SignUpView.as_view(), name='register'),
]
