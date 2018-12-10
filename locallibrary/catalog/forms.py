from random import choices

from django import forms

class RecherchForm (forms.Form):
    type = forms.CharField()
    prix = forms.CharField()

