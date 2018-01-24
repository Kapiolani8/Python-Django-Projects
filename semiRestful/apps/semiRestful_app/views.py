from django.shortcuts import render, redirect
from .models import *

def index(request):
    # messages1 = Message.objects.all()
    # User.objects.all().delete() clears users if stuff isn't working
    return render(request, "semiRestful_app/index.html")

def register(request): 

    response = User.objects.register(
        request.POST["first"],
        request.POST["last"],
        request.POST["username"],
        request.POST["email"],
        request.POST["dob"],
        request.POST["password"], 
        request.POST["confirm"]

    )
 
    if response["valid"]: 
        request.session["user_id"] = response["user"].id 
        return redirect("/home")
    else: 
        for error_message in response["errors"]: 
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def login(request): 
    response = User.objects.login(
        request.POST["email"],
        request.POST["password"]
    )
    if response["valid"]: 
        request.session["user_id"] = response["user"].id 
        return redirect("/home")
    else: 
        for error_message in response["errors"]: 
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def home(request): 
    users = User.objects.all()
    if "user_id" not in request.session: 
        return redirect("/")
    
    user = User.objects.get(id=request.session["user_id"]) 

    
    return render(request, "semiRestful_app/home.html", {"users": users, "user" : user})

def show(request, id):
    request.session["user_id"]

    print "IM RIGHT HERE",type(request.session["user_id"])
    your_users = User.objects.filter(id=id) #utilize .delete() added to the your_users = User.objects.filter(id=id) and that will delete the specific the specific id 
    print your_users
    context = {
        "users" : User.objects.all(),
        "user" : User.objects.get(id=request.session["user_id"]),
        "your_users" :  your_users
    }

    return render(request, "semiRestful_app/show.html",context)

def edit(request):
    pass 

def add_newUser(request):
    pass


def logout(request): 
    request.session.clear()
    return redirect("/")