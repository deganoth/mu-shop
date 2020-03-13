from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


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
    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    # checks cart quantity update value against exisiting product quantities

    if quantity > 0:
        if quantity <= product.quantity:
            cart[id] = quantity
            messages.success(request, "Quantity successfully updated in your cart!")
        else:
            messages.success(request, "Quantity unavailable!")
    else:
        cart.pop(id)
        messages.success(request, "Item successfully removed from your cart!")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
