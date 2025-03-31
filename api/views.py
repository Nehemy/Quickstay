from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from listings.models import Property
from .serializers import *


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            {"message": "User successfully registered."},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.profile.user_type != 'host':
            raise PermissionDenied("Only hosts can create properties.")
        serializer.save(host=self.request.user.profile)
    
    def perform_update(self, serializer):
        property_obj = self.get_object()
        if property_obj.host != self.request.user.profile:
            raise PermissionDenied("You are not allowed to update this property.")
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.host != self.request.user.profile:
            raise PermissionDenied("You are not allowed to delete this property.")
        instance.delete()