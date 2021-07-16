from django import forms
from .models import Manager

class ManagerForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}),label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}),label='Last Name')
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Age'}),label='Age')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email', 'type': 'email'}))
    contactno = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Contact No.'}),label='Contact No.')
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Manager
        fields = "__all__"
        widgets = {
            'room': forms.SelectMultiple(attrs={'class': 'custom-select'}),
        }
        labels = {
            'room': 'ROOM (multiple option available) :',
        }