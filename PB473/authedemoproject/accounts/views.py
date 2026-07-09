from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from django.urls import reverse

# Create your views here.
def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("dashboard")
        
    form = UserCreationForm()
    return render(request , "signup.html" , {"form" : form})


def dashboard(request):
    return render(request , "dashboard.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            login(request , form.get_user)
        return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request , "login.html" , {"form" : form})