from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages 

def index(request):
    # messages1 = Message.objects.all()
    # User.objects.all().delete() clears users if stuff isn't working
    return render(request, "blackBeltExam2_app/index.html")

def register(request): 

    response = User.objects.register(
        request.POST["name"],
        request.POST["alias"],
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
    users = User.objects.all().exclude(id = request.session["user_id"]) 
    if "user_id" not in request.session: 
        return redirect("/")
    
    # user1 = User.objects.get(id=request.session["user_id"])
    friends = Friend.objects.filter(friend1_id = request.session["user_id"])
    for friend in friends: 
        users = users.exclude(id = friend.friend2.id) #the .exclude allows the computer to know to not include them in the table. 

   
    return render(request, "blackBeltExam2_app/home.html", {"users": users, "friends" : friends})

def addFriend(request, id): 
    # user1 = User.objects.get(id =request.session["user_id"])
    # friend = Friend.objects.filter(id= id)
    # Friend.objects.create(friend1 = user1, friend2 = friend)
    # Friend.objects.create(friend1 = friend, friend2 = user1)

    # print "IM RIGHT HERE",type(request.session["user_id"])
    # friends = Friend.objects.filter(id=id) 
    # context = {
    #     "user1" : user1,
    #     "friend" : friend,
    #     "friends" : friends
    # }
    # return render(request, "blackBeltExam_app/home.html",context)
    # return redirect('/home')

    Friend.objects.create(friend1_id = request.session["user_id"], friend2_id = id)
    Friend.objects.create(friend1_id = id, friend2_id = request.session["user_id"])

    return redirect("/home")


def show(request, id):
    request.session["user_id"]

    print "IM RIGHT HERE",type(request.session["user_id"])
    your_users = User.objects.filter(id=id) 
    print your_users
    context = {
        "users" : User.objects.all(),
        "user" : User.objects.get(id=request.session["user_id"]),
        "your_users" :  your_users
    }

    return render(request, "blackBeltExam2_app/show.html",context)

def delete(request, id):
    print id 
    Friend.objects.filter(friend2_id = id).filter(friend1_id = request.session["user_id"]).delete()
    Friend.objects.filter(friend1_id = id).filter(friend2_id = request.session["user_id"]).delete()
    return redirect('/home')
    # request.session["user_id"]

    # print "IM RIGHT HERE",type(request.session["user_id"])
    # your_users = User.objects.filter(id=id).delete() #utilize .delete() added to the your_users = User.objects.filter(id=id) and that will delete the specific the specific id 
    # print your_users
    # context = {
    #     "users" : User.objects.all(),
    #     "user" : User.objects.get(id=request.session["user_id"]),
    #     "your_users" :  your_users
    # }

    # return render(request, "blackBeltExam1_app/home.html",context)

def logout(request): 
    request.session.clear()
    return redirect("/")
