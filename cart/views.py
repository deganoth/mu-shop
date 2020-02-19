from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, 'cart.html')
    
def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart.
    """
    quantity = 1
    
    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] = int(cart[id] + quantity)
        messages.success(request, "{} Item successfully added to your cart!".format(quantity))
    else:
        cart[id] = cart.get(id, quantity)
        messages.success(request, "{} Item successfully added to your cart!".format(quantity))
    
    request.session['cart'] = cart
    return redirect(reverse('products'))
    
def adjust_cart(request, id):
    """
    Adjust quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
        messages.success(request, "Quantity successfully updated in your cart!")
    else:
        cart.pop(id)
        messages.success(request, "Item successfully removed from your cart!")
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
