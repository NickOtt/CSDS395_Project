from django import forms
from django.forms import ModelForm
from ecommerce_site.models import Listing, User, Message

class MakeListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "buyorsell", "price", "seller", "image", "tag1", "tag2", "tag3", "tag4", "tag5",)   # NOTE: the trailing comma is required 
        
class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)
        
class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms","rows":3}))
    class Meta:
        model = Message
        fields = ["body",]