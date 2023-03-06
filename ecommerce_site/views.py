from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "ecommerce_site/home.html")

def post(request):
    return render(request, "ecommerce_site/post.html")

def messages(request):
    return render(request, "ecommerce_site/messages.html")

def login(request):
    return render(request, "ecommerce_site/login.html")
