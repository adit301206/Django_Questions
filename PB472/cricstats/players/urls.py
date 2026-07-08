from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("detail/<int:player_id>" , views.detail , name="detail"),
    path("add_player/" , views.add_player , name="add_player"),
    path("edit_player/<int:player_id>" , views.edit_player , name="edit_player"),
]
