from django import forms
from .models import User_contact


class User_contact(forms.ModelForm):
    class Meta:
        model = User_contact
        fields = ["fullname", "email", "message"]
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'custom-class-fullname'}),
            'email': forms.EmailInput(attrs={'class': 'custom-class-email'}),
            'message': forms.Textarea(attrs={'class': 'custom-class-message'}),
        }
