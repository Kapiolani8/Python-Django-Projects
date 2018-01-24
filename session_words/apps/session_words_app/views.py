from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'session_words_app/index.html')

def addAword(request): 
    print request.POST
    if 'bigfont' not in request.POST:
        word = '<p style = "color:{};">{}</p>'.format(request.POST["color"], request.POST["word"])
        newWord = {
            'word' : request.POST["word"],
            'color' : request.POST["color"],
            'big' : False
        }

    else: 
        word = '<h1 style = "color:{};">{}</h1>'.format(request.POST["color"], request.POST["word"])

        newWord = {
            'word' : request.POST["word"],
            'color' : request.POST["color"],
            'big' : True
        }


    # else: 
    #     newWord1 = {
    #         'word' : request.POST["word"], 
    #         'color' : request.POST["color"],
    #         'fontsize': request.POST["bigfont"]
    #     }

    
    request.session["words"] = word
    request.session["newWord"] = newWord
    # request.session["words2"] = newWord1








    return redirect('/')