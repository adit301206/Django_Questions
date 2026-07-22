from django.shortcuts import render , redirect
from .models import Record
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout , aauthenticate
from django import forms

# Create your views here.
def home(request):
    records = Record.objects.all()

    return render(request , "home.html" , {"records" : records})


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("home")
    else:
        form = UserCreationForm()
        return render(request , "register.html" , {"form" : form})
    

def logoutUser(request):
    logout(request)

    return redirect("home")


def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            login(request , form.get_user())
            return redirect("home")
        
    else:
        form = AuthenticationForm(request)
        return render(request , "login.html" , {"form" : form})
    

class AddForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["first_name" , "last_name" , "email" , "phone" , "address" , "city"]


def addRecord(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect("home")
            
        else:
            form = AddForm()
            return render(request , "addRecord.html" , {"form" : form})