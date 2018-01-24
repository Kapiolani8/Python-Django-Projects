from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages 

def index(request):
    movies = Movie.objects.all()
    print 

    return render(request, "index.html", {"movies" : movies})

