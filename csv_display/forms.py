# from django import forms

# class UploadCSVForm(forms.Form):
#     # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

from django import forms
from .models import Image

class ImagesForm(forms.ModelForm):
    pic = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }), label = "")
    class Meta:
        model = Image
        fields = ['pic']