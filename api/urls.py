from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api-login'),
    
]