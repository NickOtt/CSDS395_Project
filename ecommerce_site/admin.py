from django.contrib import admin
from ecommerce_site.models import User, Chat, Message

# Register your models here.
admin.site.register([User, Chat, Message])