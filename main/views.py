from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Works

# Create your views here.
def index(req):
    if not req.user.is_authenticated:
        return redirect('/login')
    return render(req, 'index.html')

def hire(req):
    content = {}
    content["works"] = Works.objects.filter(id__range=("10", "15")).values()
    return render(req, 'hire.html', content)

def login(req):
    if req.method=="POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect("/")
        messages.info(req, "Credentials Invalid")
        return redirect("login")
    return render(req, "login.html")

def logout(req):
    auth.logout(req)
    return redirect('login')

def register(req):
    if req.method=="POST":
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        password2 = req.POST["password2"]
        if not username:
            messages.info(req, "Username not given")
            return redirect("register")
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(req, "Email already used")
                return redirect("register")
            if User.objects.filter(username=username).exists():
                messages.info(req, "username already used")
                return redirect("register")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect("login")
        messages.info(req, "Password not the same")
        return redirect("register")
    
    return render(req, "register.html")