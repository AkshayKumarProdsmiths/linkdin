from django import forms
from .models import GeneralInformation

class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        fields = '__all__'
        