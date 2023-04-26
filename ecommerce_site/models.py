from django.db import models
from django.utils import timezone

class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_listed = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=255) #Should change to foreign key for user
    image = models.ImageField(upload_to="pics")
    
    def __str__(self):
        """Returns a string representation of a Listing."""
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=255, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    chats = models.ManyToManyField('Chat', related_name="chats")
    
    def __str__(self):
        """Returns a string representation of a User."""
        return self.username
    
class Chat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Returns a string representation of a User."""
        return self.user.username
    
class Message(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    