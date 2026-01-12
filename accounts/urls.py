from django.urls import path
from accounts import views

urlpatterns = [

    path('', views.register_user, name="register_user"),
    path('login', views.login_user, name="login_user")
]