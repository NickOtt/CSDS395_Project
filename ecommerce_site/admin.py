from django.contrib import admin
from ecommerce_site.models import Listing, Report

# Register your models here.
admin.site.register([Listing, Report])