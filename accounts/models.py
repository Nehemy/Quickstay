from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=350, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_images/', default="images/default.png")
    
    USER_TYPES = [
        ('host' , 'Host'),
        ('renter' , 'Looking to rent')
    ]
    user_type = models.CharField(choices = USER_TYPES, max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"