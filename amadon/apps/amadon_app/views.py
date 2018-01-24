from django.shortcuts import render, redirect 

# Create your views here.

def index(request):
    return render(request, "amadon_app/index.html")

def amadon_buy(request): 
    print request.POST


    prices ={
        'product_id' : request.POST['product_id'],
        'quantity' : request.POST['quantity']
        
    }


    if request.POST["product_id"] == '1015': 
        tempPrice = 4.99
        p = tempPrice * int(request.POST['quantity'])
        request.session['price'] = p
        request.session['totalPrice'] += p

    if request.POST["product_id"] == '1016':
        tempPrice = 54.99
        p = tempPrice * int(request.POST['quantity'])
        request.session['price'] = p
        request.session['totalPrice'] += p
    
    if request.POST["product_id"] == '1017':
        tempPrice = 8.76
        p = tempPrice * int(request.POST['quantity'])
        request.session['price'] = p
        request.session['totalPrice'] += p

    # request.session['totalPrice'] += p

    return redirect('/success')

def success(request):
    
    return render(request, "amadon_app/success.html")