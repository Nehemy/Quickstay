from rest_framework import serializers
from listings.models import Property
from accounts.models import Profile
from django.contrib.auth.models import User
from accounts.models import Profile

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

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'