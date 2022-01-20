from django import forms
from .models import Survey

class Formsurvey(forms.ModelForm):
    class Meta:
        model= Survey
        fields= ["points", "desc"]