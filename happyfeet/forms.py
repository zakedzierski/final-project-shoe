from django import forms
from .models import MyShoe

class ShoeForm(forms.ModelForm):
    class Meta:
        model = MyShoe
        fields = ('name', 'brand', 'icon', 'miles_run',)
