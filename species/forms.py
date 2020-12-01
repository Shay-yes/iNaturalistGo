from django import forms
from .models import *

class SpeciesForm(forms.ModelForm):

    class Meta:
            model = Species
            fields = ['common_name', 'latin_name', 'location', 'image']


