from django import forms
from .models import SimpleComments

class SimpleCommentsForm(forms.ModelForm):
    class Meta:
        model = SimpleComments
        fields = ['nama', 'komentar']

    nama = forms.CharField(
        max_length=100,
        widget=forms.TextInput()
    )

    komentar = forms.CharField(
        widget=forms.Textarea()
    )