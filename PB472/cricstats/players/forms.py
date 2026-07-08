from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["playerName" , "country" , "battingStyle" , "bowlingStyle" , "age" , "runScored" , "wicketsTaken"]