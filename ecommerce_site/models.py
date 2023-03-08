from django.db import models
from django.utils import timezone

class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_listed = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pics")
    
    def __str__(self):
        """Returns a string representation of a Listing."""
        return "TODO"
    
class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        """Returns a string representation of a User."""
        return "TODO"