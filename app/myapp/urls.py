from django.urls import path
from . import views
from .forms import UserLoginForm
from django.contrib.auth import views as views1

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("login/", views1.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login'),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("menu/", views.menu, name="menu"),
    path("profile/", views.profile, name="profile"),
    path("order/", views.order, name="order"),
    path("balance/", views.balance, name="balance"),
    path("ordered-this-week/", views.ordered_this_week, name="ordered-this-week"),
    path("payment/", views.payment, name="payment"),
    path("create-post/", views.create_post, name="create-post"),
]
