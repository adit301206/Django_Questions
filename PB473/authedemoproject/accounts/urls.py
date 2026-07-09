from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/' , views.dashboard , name="dashboard"),
    path('signup/' , views.signup_user , name="signup"),
    path('login/' , views.login_user , name="login"),
]
