from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import auth
from django.contrib import messages as msgs
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import JsonResponse

from ecommerce_site.forms import MakeListingForm, AccountChangeForm, MessageForm, RegisterForm
from ecommerce_site.models import Listing, Message, Chat, Profile, Report

import json

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Listing

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

class LogoutView(View):
    """Redirects to home page after logout."""
    
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect("home")
    
class LoginView(View):
    """Redirects to home page after login."""
    
    def get(self, request, *args, **kwargs):
        return render(request, 'ecommerce_site/login.html')

def home(request):
    query = ""
    if request.method == "POST":
        query = request.POST['query'] 
    data = Listing.objects.filter(title__icontains=query).order_by("-time_listed")[:20]

    if query != "":
        return render(request, "ecommerce_site/home.html", {"post_list": data, "search_term": query})
    else:
        return render(request, "ecommerce_site/home.html", {"post_list": data})

def report(request, pk):
    if not request.user.is_authenticated:
        return redirect("home")
    
    Report.objects.create(listing=Listing.objects.get(id=pk))
    
    # msgs.info(request, "Listing has been reported") to be implemented later
    
    return redirect("home")

def post(request):
    form = MakeListingForm(request.POST or None, request.FILES or None)
    
    # Redirect user to home page if not logged in
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        s = form.errors

        if form.is_valid():
            listing = form.save(commit=False)
            listing.title = request.POST['title']
            listing.price = request.POST['price']
            listing.seller = request.POST['seller']
            listing.seller_user = request.user
            listing.time_listed = datetime.now()
            listing.image = request.FILES['image']
            listing.save()
            return redirect("post_success", pk=listing.pk)
        else:        
            return render(request, "ecommerce_site/post.html", {'error': "Bad input!"})

    else:
        return render(request, "ecommerce_site/post.html", {"form": form})
  
    
def post_success(request, pk):
    # Redirect user to home page if not logged in
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        return redirect("home")
    else:
        listing = Listing.objects.get(pk=pk)
        return render(request, 'ecommerce_site/post_success.html', {'listing' : listing})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            
            Profile.objects.create(user_id = User.objects.get(username=form.data["username"]).id)
            
        return redirect("login")
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})

def delete_listing(request, pk):
    Listing.objects.get(pk=pk).delete()
    return redirect("account")

def account(request):
    form = AccountChangeForm(request.POST or None)
    
    # Redirect user to home page if not logged in
    if not request.user.is_authenticated:
        return redirect("home")
    listings = Listing.objects.filter(seller_user = request.user)

    if request.method == "POST":
        s = form.errors

        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect("account", {'post_list' : listings})
        else:        
            return render(request, "ecommerce_site/account.html", {'error': "Bad input!", 'post_list' : listings})

    else:
        return render(request, "ecommerce_site/account.html", {"form": form, 'post_list' : listings})

def messages(request):
    # Redirect user to home page if not logged in
    if not request.user.is_authenticated:
        return redirect("home")
    
    user = request.user.profile
    chat_list = user.chats.all()
    context= {"user": user, "chat_list": chat_list}
    
    return render(request, "ecommerce_site/messages.html", context)

def detail_messages(request, pk):
    user = request.user.profile
    
    if not Chat.objects.filter(profile_id=pk).exists():
        new_chat = Chat.objects.create(profile_id=pk)
        user.chats.add(new_chat)
        user.save()
        
    if not user.chats.filter(profile_id=pk):
        existing_chat = Chat.objects.get(profile_id=pk)
        user.chats.add(existing_chat)
        user.save()
        
    chat = Chat.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=chat.profile.id)
        
    if not Chat.objects.filter(profile_id=user.id).exists():
        new_chat2 = Chat.objects.create(profile_id=user.id)
        profile.chats.add(new_chat2)
        profile.save()  
        
    if not profile.chats.filter(profile_id=user.id):
        existing_chat = Chat.objects.get(profile_id=user.id)
        profile.chats.add(existing_chat)
        profile.save()
        
    message_list = Message.objects.all()
    recent_messages = Message.objects.filter(from_user=profile, to_user=user, seen=False)
    recent_messages.update(seen=True)
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.from_user = user
            message.to_user = profile
            message.save()
            return redirect("detail_messages", pk=chat.profile.id)
    context = {"chat": chat, "form": form, "user": user, "profile":profile, "message_list":message_list, "num": recent_messages.count()}
    return render(request, "ecommerce_site/detail_messages.html", context)

def sent_messages(request, pk):
    user = request.user.profile
    chat = Chat.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=chat.profile.id)
    data = json.loads(request.body)
    new_message = data["msg"]
    new_message_body = Message.objects.create(message=new_message, from_user=user, to_user=profile, seen=False)
    print(new_message)
    return JsonResponse(new_message_body.message, safe=False)
    
def received_messages(request, pk):
    user = request.user.profile
    chat = Chat.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=chat.profile.id)
    message_arr = []
    message_list = Message.objects.filter(from_user=profile, to_user=user, seen=False)
    for message in message_list:
        message_arr.append(message.message)
    message_list.update(seen=True)
    return JsonResponse(message_arr, safe=False)