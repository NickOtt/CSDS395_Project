from django.urls import path, include
from ecommerce_site import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("report/<str:pk>", views.report, name="report"),
    path("messages/", views.messages, name="messages"),
    path('chat/<str:pk>', views.detail_messages, name="detail_messages"),
    path('sent_msg/<str:pk>', views.sent_messages, name = "sent_msg"),
    path('rec_msg/<str:pk>', views.received_messages, name = "rec_msg"),
    path('post_success/<int:pk>', views.post_success, name='post_success'),
    path('register/', views.register, name="register"),
    path("account/", views.account, name="account"),
    path("delete_listing/<int:pk>", views.delete_listing, name="delete_listing"),
    
    path("", include("django.contrib.auth.urls")),
    #path("login/", views.LoginView.as_view(), name="login"),
    #path("logout/", views.LogoutView.as_view(), name="logout"),
]