from django.urls import path
from ecommerce_site import views
from ecommerce_site.models import Listing

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("messages/", views.messages, name="messages"),
    path('post_success/<int:pk>', views.post_success, name='post_success'),
    path("account/", views.account, name="account"),
    #path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]