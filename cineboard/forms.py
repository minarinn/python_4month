from django import forms
from . import models

class FilmsForm(forms.ModelForm):
    class Meta:
        model = models.Films
        fields = ['title', 'description', 'genre', 'release_date', 'tags']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.SelectMultiple(),
        }
