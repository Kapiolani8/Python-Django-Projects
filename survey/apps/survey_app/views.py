from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'survey_app/index.html')

def process(request): 
    # try: 
    #     request.session["count"] += 1 
    # except KeyError as e: 
    #     request.session["count"] = 0 
    if 'count' not in request.session: 
        request.session["count"] = 0
    request.session["count"] += 1 
    request.session["name"] = request.POST["name"]
    request.session["favlang"] = request.POST["favlang"]
    request.session["location"] = request.POST["location"]
    request.session["comment"] = request.POST["comment"]
    return redirect('/result')

def result(request):
    return render(request, "survey_app/result.html")