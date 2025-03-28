from django.db import models
import uuid
from accounts.models import Profile
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError

class Property(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="properties", null=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
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
    cover_image = models.ImageField(null=True, blank=True, upload_to='cover_images/', default="images/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.property_type} in {self.city} - {self.id}"
    
class PropertyImage(models.Model):
    
        def validate_image(file):
            filesize = file.size
            megabyte_limit = 10.0
            if filesize > megabyte_limit * 1024 * 1024:
                raise ValidationError(f"Maximum file size is {megabyte_limit}MB")
            
            valid_mimetypes = ['image/jpeg', 'image/png', 'image/gif']
            
            if file.content_type not in valid_mimetypes:
                raise ValidationError("Unsupported file type. Only JPEG, PNG and GIF are allowed.")
            
        property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
        image = models.ImageField(upload_to='property_images/', null=True, blank=True, validators=[validate_image])
        
        
        def __str__(self):
            return f"Cover image for {self.property.title} - {self.property.id}"

class Enquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="enquiries")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)