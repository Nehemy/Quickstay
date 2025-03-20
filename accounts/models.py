from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    
    USER_TYPES = [
        ('host' , 'Host'),
        ('renter' , 'Looking to rent')
    ]
    user_type = models.CharField(choices = USER_TYPES, max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)