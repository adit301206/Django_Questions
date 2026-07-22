from django.shortcuts import render , redirect , get_object_or_404
from .models import Record
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout , aauthenticate
from django import forms
from django.contrib.auth.decorators import login_required

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
        

@login_required
def updateRecord(request , record_id):
    record = get_object_or_404(Record , pk = record_id)

    if request.method == "POST":
        form = AddForm(request.POST , instance=record)

        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        form = AddForm(instance=record)
        return render(request , "updateRecord.html" , {"form" : form})
    

@login_required
def deleteRecord(request , record_id):
    record = get_object_or_404(Record , pk = record_id)
    # record.delete()
    # return redirect("home")

    if request.method == "POST":
        record.delete()
        return redirect("home")
    else:
        return render(request , "delete.html" , {"data" : record})