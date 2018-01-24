from django.shortcuts import render
import random 

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# Create your views here.

def index(request):
    return render(request, "randomWord_app/index.html")

def makeAword(request):
    if 'count' not in request.session: 
        request.session["count"] = 0
    request.session["count"] += 1 
    request.session["word"] = generateWord(8)
    return render(request,"randomWord_app/index.html")

def generateWord(num): 
    string = ''
    for i in range(num): 
        string += ALPHABET[random.randrange(0,26)]
    
    return string
