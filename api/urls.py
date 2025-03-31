from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='properties')
router.register(r'enquiries', EnquiryViewSet, basename='enquiries')
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('login/', obtain_auth_token, name='api-login'),
    
    path('public-profile/<str:pk>/', PublicProfileAPIView.as_view(), name='api-public-profile'),
    
]