from django import forms
from . import models


class qrcodes(forms.ModelForm):
    class Meta:
        model = models.qrcodes
        fields = ["text_input"]