from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(redirect): #or request????
    return redirect('/')

def show(request, blog_id):
    return HttpResponse('placeholder to display blog {{}})'.format(blog_id))

def edit(request, blog_id):
    return HttpResponse('placeholder to edit blog {{}})'.format(blog_id))

def destroy(request):
    return redirect('/')
