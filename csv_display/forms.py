from django import forms

class UploadCSVForm(forms.Form):
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
