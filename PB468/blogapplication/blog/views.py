from django.shortcuts import render , redirect
from .models import Post
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

# Create your views here.
def home(request):
    data = Post.objects.all()

    return render(request , "home.html" , {"data" : data})


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title" , "content" , "author"]


@login_required
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = PostForm()
        return render(request , "createPost.html" , {"form" : form})
    

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            login(request , form.get_user())
            return redirect("home")
        else:
            form = AuthenticationForm(request)
            return render(request , "login.html" , {"form" : form})
    else:
        form = AuthenticationForm(request)
        return render(request , "login.html" , {"form" : form})
    

def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("home")
        
    form = UserCreationForm()
    return render(request , "register.html" , {"form" : form})