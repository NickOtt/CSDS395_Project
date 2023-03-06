from django.urls import path
from ecommerce_site import views

urlpatterns = [
    path("", views.home, name="home"),
    path("listings/", views.listings, name="listings"),
    path("messages/", views.messages, name="messages"),
    path("login/", views.login, name="login"),
]