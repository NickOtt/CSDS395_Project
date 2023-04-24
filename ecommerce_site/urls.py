from django.urls import path
from ecommerce_site import views
from ecommerce_site.models import Listing

home_list_view = views.HomeListView.as_view(
    queryset= Listing.objects.order_by("-time_listed")[:10],  # :5 limits the results to the five most recent
    context_object_name="post_list",
    template_name="ecommerce_site/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("post/", views.post, name="post"),
    path("messages/", views.messages, name="messages"),
    path('post_success/<int:pk>', views.post_success, name='post_success'),
    path("account/", views.account, name="account"),
    #path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]