from django.urls import path
from ecommerce_site import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("messages/", views.messages, name="messages"),
    path("login/", views.login, name="login"),
]