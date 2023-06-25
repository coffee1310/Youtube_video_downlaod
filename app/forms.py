from .models import *
from django import forms

class Link(forms.Form):
    class Meta:
        model = Link
        fields = ["link"]
        widgets = {
            'link':forms.TextInput(attrs={"class":"link"}),
        }