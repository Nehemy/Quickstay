from rest_framework import serializers
from listings.models import *
from accounts.models import Profile
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    user_type = serializers.ChoiceField(choices=Profile.USER_TYPES)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password', 'password2', 'user_type')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    
    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        validated_data.pop('password2')
        name = validated_data.pop('name')
        
        user = User(
            username=validated_data['username'].lower(),
            email=validated_data['email'],
            first_name=name
        )
        user.set_password(validated_data['password'])
        user.save()
        
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=name,
            user_type=user_type
        )
        return user
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']
        

class PropertySerializer(serializers.ModelSerializer):
    
    class EnquirySerializer(serializers.ModelSerializer):
        class Meta:
            model = Enquiry
            fields = '__all__'
        

    images = PropertyImageSerializer(many=True, read_only=True)
    enquiries = serializers.SerializerMethodField()
                                     
    class Meta:
        model = Property
        fields = '__all__'
    
    def get_enquiries(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if obj.host == request.user.profile:
                serializer = self.EnquirySerializer(obj.enquiries.all(), many=True)
                return serializer.data
        return []
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'name', 'email', 'bio', 'profile_picture', 'user_type', 'date_joined', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email', 'profile')
