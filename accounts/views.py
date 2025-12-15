from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . models import User
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.decorators import login_required



# Create your views here.

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 1. Password match check
        if password1 != password2:
            return render(request, "auth/register.html", {
                "error": "Passwords must match"
            })

        # 2. Email exists check
        if User.objects.filter(email=email).exists():
            return render(request, "auth/register.html", {
                "error": "Email is already registered"
            })

        # 3. Generate username safely
        base_username = email.split("@")[0]
        username = base_username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        # 4. Create user (CORRECT variables)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect("/accounts/login/")

    return render(request, "auth/register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            
            return render(request,"mainservice/form.html" )
        else:
            return render(request, "auth/login.html", {
                "error": "Invalid email or password"
            })

    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)          # destroys the session
    return redirect("/")  

# @login_required(login_url="/accounts/login/")
# def dashboard_view(request, user):

#     return render(request, "mainservice/form.html" )
    