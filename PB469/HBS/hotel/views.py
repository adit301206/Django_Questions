from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request , "home.html" , {"rooms" : rooms})


def logoutUser(request):
    logout(request)
    return redirect("home")


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
    

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            login(request , form.get_user())
            return redirect("home")
        
    else:
        form = AuthenticationForm(request)
        return render(request , "login.html" , {"form" : form})
    

def book_room(request , room_id):
    room = get_object_or_404(Room , id=room_id)
    Booking.objects.create(user = request.user , room = room , is_paid = True)
    return redirect("home")


def review(request , room_id):
    room = get_object_or_404(Room , pk = room_id)

    if request.method == "POST" and request.user.is_authenticated:
        rating_value = request.POST.get('rating')
        # comment_text = request.POST.get('comment')
        Review.objects.create(user=request.user, room=room, rating=rating_value)
        return redirect('reviews', room_id=room_id)
    
    room_reviews = Review.objects.filter(room = room)
    return render(request , "review.html" , {"room" : room , "reviews" : room_reviews})