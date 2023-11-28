from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from .models import Menu

# Create your views here.
def home(request):
    return render(request, "main/home.html")

@login_required(login_url="/login")
#@permission_required("myapp | menu | Can add menu", login_url="/menu")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.author = request.user
            menu.save()
            return redirect("/menu")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})
    

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/menu')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
def menu(request):
    menus = Menu.objects.all()

    if request.method == "POST":
        menu_id = request.POST.get("menu-id")
        menu = Menu.objects.filter(id=menu_id).first()
        if menu and menu.author == request.user:
            menu.delete()

    return render(request, "main/menu.html", {"menus": menus})

@login_required(login_url="/login")
def profile(request):
    return render(request, "main/profile.html")

@login_required(login_url="/login")
def order(request):
    return render(request, "main/order.html")

@login_required(login_url="/login")
def balance(request):
    return render(request, "main/balance.html")

@login_required(login_url="/login")
def ordered_this_week(request):
    return render(request, "main/ordered-this-week.html")

@login_required(login_url="/login")
def payment(request):
    return render(request, "main/payment.html")
