from django.db import models
import uuid
from accounts.models import Profile
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator

class Property(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        ('studio', 'Studio'),
        ('hotel', 'Hotel'),
        ('hostel', 'Hostel'),
    ]
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    AMENITY_CHOICES = [
        ('wifi', 'WiFi'),('ac', 'Air Conditioning'),('heating', 'Heating'),('kitchen', 'Kitchen'),('parking', 'Parking'),('washer', 'Washer'),('dryer', 'Dryer'),('tv', 'TV'),('pool', 'Pool'),('gym', 'Gym'),('breakfast', 'Breakfast Included'),('pets', 'Pets Allowed'),('smoking', 'Smoking Allowed'),('elevator', 'Elevator'),('wheelchair', 'Wheelchair Accessible'),('hottub', 'Hot Tub'),('sauna', 'Sauna'),('bbq', 'BBQ Grill'),('fireplace', 'Fireplace'),('balcony', 'Balcony'),('garden', 'Garden'),('private_entrance', 'Private Entrance'),('cable_tv', 'Cable TV'),('coffee_maker', 'Coffee Maker'),('iron', 'Iron'),('hair_dryer', 'Hair Dryer'),('luggage_drop', 'Luggage Drop Off'),('essentials', 'Essentials (towels, bed sheets, soap, and toilet paper)'),('workspace', 'Laptop Friendly Workspace'),('self_check_in', 'Self Check-in'),('family_friendly', 'Family/Kid Friendly'),
        ]
    amenities = MultiSelectField(choices=AMENITY_CHOICES, max_length=500, blank=True, null=True)
    cover_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.id}"
    
class PropertyImage(models.Model):
        property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
        cover_image = models.ImageField(upload_to='property_cover_images/', null=True, blank=True)
        
        def __str__(self):
            return f"Cover image for {self.property.title} - {self.property.id}"
    
class Review(models.Model):
        id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
        property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
        reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
        rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
        comment = models.TextField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return f"{self.rating} star review by {self.reviewer.user.username} on {self.property.title}"

class Enquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="enquiries")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)