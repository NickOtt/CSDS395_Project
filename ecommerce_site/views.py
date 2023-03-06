from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "ecommerce_site/home.html")

def post(request):
    return render(request, "app/post.html")

def messages(request):
    return render(request, "app/messages.html")

def login(request):
    return render(request, "app/login.html")
