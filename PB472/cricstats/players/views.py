from django.shortcuts import render , get_object_or_404 , redirect
from .models import Player
from .forms import PlayerForm
from django.http import HttpResponseForbidden , HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    players = Player.objects.all()

    return render(request , "home.html" , {"data" : players})


def detail(request , player_id):
    player = get_object_or_404(Player , pk = player_id)

    return render(request , "detail.html" , {'data' : player})


def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PlayerForm()
        return render(request , "addplayer.html" , {"form" : form})
    

def edit_player(request , player_id):
    player = get_object_or_404(Player , pk = player_id)

    if player:
        if request.method == "POST":
            form = PlayerForm(request.POST , instance=player)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('detail' , args=[player_id]))
            
        else:
            form = PlayerForm(instance=player)
            return render(request , "editplayer.html" , {"form" : form , "data" : player})
        

def delete_player(request , player_id):
    player = get_object_or_404(Player , pk = player_id)

    if request.method == "POST":
        player.delete()
        return redirect("home")
    
    return render(request , "deleteplayer.html" , {"data" : player})