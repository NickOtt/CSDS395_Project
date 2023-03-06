from django.shortcuts import render

def home(request):
    return render(request, "ecommerce_site/home.html")

def listings(request):
    return render(request, "app/listings.html")

def messages(request):
    return render(request, "app/messages.html")

def login(request):
    return render(request, "app/login.html")
