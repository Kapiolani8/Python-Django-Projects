from django.shortcuts import render, redirect
from .models import User, Message
from django.contrib import messages

def index(request):
    messages1 = Message.objects.all()
    # User.objects.all().delete() clears users if stuff isn't working
    return render(request, "beltReview_app/index.html", {"messages1": messages1})

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



def logout(request): 
    request.session.clear()
    return redirect("/")

def home(request): 
    if "user_id" not in request.session: 
        return redirect("/")

    context = { 
        "user" : User.objects.get(id=request.session["user_id"]), 
        "users": User.objects.all().exclude(id=request.session["user_id"]), 
        "your_messages": Message.objects.filter(received_by=request.session["user_id"])
    }
    return render(request, "beltReview_app/home.html", context)
    
def new_message(request, id): 
    print id
    return render(request, "beltReview_app/new_message.html", {"id": id})

def add_message(request, id): 
    new_message = Message.objects.sendMessage(
        request.POST["content"], 
        request.session["user_id"],
        id
        )
    print new_message 
    if type(new_message) is unicode: 
        messages.add_message(request, messages.ERROR, new_message)
        return redirect("/message/" + str(id))
    return redirect("/home")

def view_messages(request): 
    your_messages =  Message.objects.filter(received_by=request.session["user_id"])

    return render(request, "beltReview_app/messages.html", {"your_messages" : your_messages})