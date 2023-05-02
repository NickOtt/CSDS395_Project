from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chats = models.ManyToManyField('Chat', related_name="chats")
    
    def __str__(self):
        return self.user.username
    
class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_listed = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=255)
    buyorsell = models.CharField(max_length=5, default='sell')
    seller_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="seller")
    image = models.ImageField(upload_to="pics")
    
    def __str__(self):
        """Returns a string representation of a Listing."""
        return self.title
    
class Chat(models.Model):
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        """Returns a string representation of a User."""
        return self.profile.user.username
    
class Message(models.Model):
    to_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="from_user")
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
    
class Report(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing")
    
    def __str__(self):
        return self.listing.title
    