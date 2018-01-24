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
    # users = User.objects.all().exclude(id = request.session["user_id"]) 
    if "user_id" not in request.session: 
        return redirect("/")
    
    quotes = Quote.objects.all()
    favorites = Favorite.objects.filter(user_id = request.session["user_id"])

    for x in favorites: 
        quotes = quotes.exclude(id = x.quote.id)


    return render(request, "blackBeltExam2_app/home.html", {"quotes": quotes, "favorites": favorites})

   
    return render(request, "blackBeltExam2_app/home.html")

def addToFavorites(request, id): 

    Favorite.objects.create(user_id = request.session["user_id"] , quote_id = id) 

    return redirect('/home')


def addQuote(request, methods = 'POST'):
    
    quote = Quote.objects.addQuote(request.POST["author"], request.POST["quote"], request.session["user_id"])
    print type(quote)

    if type(quote) is list: 
        for error_message in quote: 
            messages.add_message(request, messages.ERROR, error_message)

    else: 
        Favorite.objects.create(user_id = request.session["user_id"] , quote_id = quote.id) 
    


    # print author, quote
    # errors = []
    # if len(request.POST["author"]) < 2:
    #     errors.append('Author must be 3 characters or more')
    # if  len(request.POST["quote"]) < 10:
    #     errors.append("Quote must be more than 10 characters")
    # if len(errors) > 0: 
    #     return errors 
    # else: 
    # #     return Quote.objects.create(author=author, quote=quote)
    
    # author = Quote.objects.create(author=request.POST["author"])
    # quote = Quote.objects.create(quote=request.POST["quote"])
    # request.session["author"] = request.POST["author"]
    # request.session["quote"] = request.POST["quote"]

    return redirect('/home')

def user(request, id): 
    request.session["user_id"] 

    print "IM RIGHT HERE",type(request.session["user_id"])
    your_users = User.objects.filter(id=id) 
    print your_users
    context = {
        "users" : User.objects.all(),
        "user" : User.objects.get(id=request.session["user_id"]),
        "your_users" :  your_users, 
        "quoted_by" : Quote.objects.filter(quoted_by = id)
    }
    

    return render(request, "blackBeltExam3_app/show.html", context)
def delete(request, id):
    print id 
    Favorite.objects.filter(id = id).delete()
    return redirect('/home')

def logout(request): 
    request.session.clear()
    return redirect("/")