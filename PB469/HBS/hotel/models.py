from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField()