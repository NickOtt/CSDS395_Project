from datetime import datetime
from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import auth
from django.urls import reverse
from django.views.generic import View

from ecommerce_site.forms import MakeListingForm
from ecommerce_site.models import Listing

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
    
def post(request):
    form = MakeListingForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        s = form.errors

        if form.is_valid():
            listing = form.save(commit=False)
            listing.title = request.POST['title']
            listing.price = request.POST['price']
            listing.seller = request.POST['seller']
            listing.time_listed = datetime.now()
            listing.image = request.FILES['image']
            listing.save()
            return redirect("post_success", pk=listing.pk)
        else:        
            return render(request, "ecommerce_site/post.html", {'error': "Bad input!"})

    else:
        return render(request, "ecommerce_site/post.html", {"form": form})
    
    
def post_success(request, pk):

    if request.method == "POST":
        return redirect("home")
    else:
        listing = Listing.objects.get(pk=pk)
        return render(request, 'ecommerce_site/post_success.html', {'listing' : listing})

def account(request):
    return render(request, "ecommerce_site/account.html")

def messages(request):
    return render(request, "ecommerce_site/messages.html")
