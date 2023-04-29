from django import forms
from django.forms import ModelForm
from ecommerce_site.models import Listing, User, Message, Tag

class MakeListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "buyorsell", "price", "tags", "image",)   # NOTE: the trailing comma is required 
        
    buyorsell=forms.Select(choices=["Requesting", "Selling"])
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    # Overriding __init__ here allows us to provide initial data for 'toppings' field
    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
                        
            initial = kwargs.setdefault('initial', {})
            initial['tags'] = [t.pk for t in kwargs['instance'].tag_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field    
    def save(self, commit=True):
        # Get the unsave Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           # This is where we actually link the pizza with toppings
           instance.tag_set.clear()
           instance.tag_set.add(*self.cleaned_data['toppings'])
        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance
    
        
class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)
        
class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms","rows":3}))
    class Meta:
        model = Message
        fields = ["body",]