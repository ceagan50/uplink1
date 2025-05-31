from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Sermon, Event,  ContactMessage

class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ['title', 'preacher', 'date_preached',  'video_file', 'description']
        widgets = {
            'date_preached': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'image', 'is_featured']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ['title', 'preacher', 'date_preached', 'description', 
             'video_file']
        widgets = {
            'date_preached': forms.DateInput(attrs={'type': 'date'}),
        }