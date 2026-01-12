from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

# Create your views here.


def register_user(request):

    errors = {}

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmpassword")

        if not username:
            errors["username"] = "Username is required"

        elif User.objects.filter(username=username).exists():
            errors["username"] = "Username already exists"

        if not password or not confirm_password:
            errors["password"] = "Password is required"

        elif password != confirm_password:
            errors["password"] = "Password do not match"
        
        # try:
        #     validate_password(password)
        # except ValidationError as e:
        #     errors["password"] = e.messages
    

        if not errors:

            User.objects.create_user(username=username, password=password)
            return redirect('login_user')
        
        else:

            form_data = request.POST 
            context = {
                'form_data':form_data,
                'errors':errors.values(),
            }   
            return render(request, "accounts/register.html",context=context)
    else:
        return render(request, "accounts/register.html")
    

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Generator:index')
        else:
            form_data = request.POST
            return render(request, "accounts/login.html", {'error':'Invalid Username or Password', 'form_data':form_data})
    
    else:
        return render(request, "accounts/login.html")
    
