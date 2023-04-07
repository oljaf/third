from django import forms
from .models import *

class Video_form(forms.ModelForm):
    class Meta:
        model=Video
        fields=("caption","video")
