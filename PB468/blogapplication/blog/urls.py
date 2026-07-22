from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('create/' , views.createPost , name="createPost"),
    path('logout/' , views.logoutUser , name="logout"),
    path('login/' , views.loginUser , name="login"),
    path('register/' , views.registerUser , name="register"),
]
