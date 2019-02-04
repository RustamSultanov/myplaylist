from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .models import Track
from django.db import models
from audiofield.widgets import CustomerAudioFileWidget

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={'id': "email",
               'class': "validate"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}))


class EditTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name', 'artist', 'rating', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'artist': forms.TextInput(attrs={'class': 'form-control', }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'custom-select', }),
        }


class UploadTrackForm(EditTrackForm):
    audio_file = forms.FileField(
        widget=CustomerAudioFileWidget(attrs={'class': 'form-control'}))

    class Meta(EditTrackForm.Meta):
        model = Track
        fields = ['name', 'artist', 'rating', 'image', 'audio_file']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_picture']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', }),
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'profile_picture': forms.FileInput()
        }
