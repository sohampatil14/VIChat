from django import forms
from .models import connection

class connectionForm(forms.ModelForm):
    class Meta:
        model = connection
        fields = ['name', 'profile_photo', 'is_started']
        widgets = { 
            'password': forms.PasswordInput()
            }