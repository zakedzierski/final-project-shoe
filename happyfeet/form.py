from django import forms
from django.forms import ModelForm
from contact.models import Suggestion

class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        exclude = ('approved',)
