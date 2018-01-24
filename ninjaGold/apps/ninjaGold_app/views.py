from django.shortcuts import render, redirect
from random import randrange

# Create your views here.
def index(request):
    if 'gold' not in request.session: 
        request.session['gold'] = 0 
    if 'activity' not in request.session: 
        request.session['activity'] = []
    return render(request, "ninjaGold_app/index.html")

def process_gold(request, location):
    print location
    if location == 'farm': 
        gold = randrange(10,21)
            
    elif location == 'cave': 
        gold = randrange(5,50)
        
    elif location == 'house': 
        gold = randrange(11,101)
        
    else: 
        gold = randrange(-50,51)
    
    if gold >= 0: 
        verb = "earned"
    else: 
        verb = "lost"

    request.session['activity'].append('You went to the {} and {} {} gold'.format(location, verb, abs(gold)))
    request.session['gold'] += gold
    return redirect('/')