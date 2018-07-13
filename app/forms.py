from django import forms
import datetime
from django.forms import widgets
from app.models import VendorListing, Lala


class VendorListingForm(forms.ModelForm):
    class Meta:
        model = VendorListing
        fields = ('dateServing','Name', 'location','Address','zipCode','beginning', 'ending','city', 'userlocation')


class DateInput(forms.DateInput):
    input_type = 'date'


class LalaForm(forms.ModelForm):

    class Meta:
        model = Lala
        fields = ('name', 'date','priority','color','beginning', 'ending')
        widgets = {
            'date': DateInput(),
        }
