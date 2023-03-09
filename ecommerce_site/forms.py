from django import forms
from ecommerce_site.models import Listing, User

class MakeListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "price", "seller", "image",)   # NOTE: the trailing comma is required 
        
class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)