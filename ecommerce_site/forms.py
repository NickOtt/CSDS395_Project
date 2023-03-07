from django import forms
from ecommerce_site.models import Listing

class MakeListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "price", "seller",)   # NOTE: the trailing comma is required 