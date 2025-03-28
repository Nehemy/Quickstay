from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

USER_TYPE_CHOICES = [
    ('', '--- Select a user type ---'),
    ('host', 'Host'),
    ('renter', 'Looking to rent'),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label="Select Account Type")
    
    class Meta:
        model = User
        fields = ("username", "first_name", "user_type", "email", "password1", "password2")
        labels = {
            "username": "Username",
            'first_name': "Name",
            "email": "Email Address",
            "password1": "Enter Your Password",
            "password2": "Confirm Your Password",
        }
    
    def clean_first_name(self):
        name = self.cleaned_data.get('first_name')
        if not name.isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters.")
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.username.lower()
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.user_type = self.cleaned_data["user_type"]
            user.profile.save()
        return user
