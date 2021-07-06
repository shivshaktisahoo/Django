from django import forms
from .models import Vacationtrip

class VacationtripForm(forms.ModelForm):
    class Meta:
        model = Vacationtrip
        fields = "__all__"