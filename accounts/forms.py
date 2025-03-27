from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")
        labels = {
            "username": "Username",
            'first_name': 'Name',
            "email": "Email Address",
            "password1": "Enter Your Password",
            "password2": "Confirm Your Password",
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.username.lower()
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
