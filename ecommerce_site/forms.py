from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ecommerce_site.models import Listing, Message

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]

class MakeListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "price", "seller", "image",)   # NOTE: the trailing comma is required 
        
class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)
        
class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms","rows":3}))
    class Meta:
        model = Message
        fields = ["body",]