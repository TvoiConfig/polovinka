from django import forms
from .models import *



class RecordForm(forms.ModelForm):
    success_url = 'about'
    class Meta:
        model = record
        fields = ['name', 'number', 'message']