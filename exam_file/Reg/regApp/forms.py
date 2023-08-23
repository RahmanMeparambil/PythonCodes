from django import forms
from .models import Registration

class NewReg(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('FirstName','LastName','Image',)

class EditReg(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('FirstName','LastName','Image',)