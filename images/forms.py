from django import forms


class UploadForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    file = forms.ImageField(label='Image')
