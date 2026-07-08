from django.db import models

# Create your models here.
class Player(models.Model):
    playerName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    battingStyle = models.CharField(max_length=30)
    bowlingStyle = models.CharField(max_length=50)
    age = models.IntegerField()
    runScored = models.IntegerField()
    wicketsTaken = models.IntegerField()

    def __str__(self):
        return self.playerName