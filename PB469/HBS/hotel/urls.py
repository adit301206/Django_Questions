from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('logout/' , views.logoutUser , name="logout"),
    path('register/' , views.registerUser , name="register"),
    path('login/' , views.loginUser , name="login"),
    path('book/<int:room_id>/' , views.book_room , name="bookroom"),
    path('reviews/<int:room_id>/' , views.review , name="reviews"),
]
