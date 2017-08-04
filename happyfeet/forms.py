from django import forms
from .models import MyShoe

class ShoeForm(forms.ModelForm):
    class Meta:
        model = MyShoe
        fields = ('name', 'brand', 'icon', 'miles_run')


class AddMilesForm(forms.ModelForm):
    class Meta:
        model = MyShoe
        fields = ('miles_run',)
