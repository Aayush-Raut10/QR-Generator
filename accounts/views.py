from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    return render(request, "accounts/login.html")


def register_user(request):
    return render(request, "accounts/register.html")