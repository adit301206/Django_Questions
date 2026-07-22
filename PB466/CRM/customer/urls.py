from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('register/' , views.registerUser , name="register"),
    path('logout/' , views.logoutUser , name="logout"),
    path('login/' , views.loginUser , name="login"),
    path('addrecord/' , views.addRecord , name="addrecord"),
    path('update/<int:record_id>/' , views.updateRecord , name="update"),
    path('delete/<int:record_id>/' , views.deleteRecord , name="delete"),
]
