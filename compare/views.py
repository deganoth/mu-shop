from django.shortcuts import render, redirect, reverse

def view_compare(request):
    """
    A view that renders the cart contents page
    """
    return render(request, 'compare.html')
    
def add_to_compare(request, id):
    """
    Add a quantity of the specified product to the cart.
    """
    quantity = 1
    
    compare = request.session.get('compare', {})
    
    if id in compare:
        compare[id] = 1
    else:
        compare[id] = compare.get(id, quantity)
        
    request.session['compare'] = compare
    return redirect(reverse('products'))
    
def adjust_compare(request, id):
    """
    Adjust quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    
    compare = request.session.get('compare', {})
    
    if quantity > 0:
        compare[id] = quantity
    else:
        compare.pop(id)
        
    request.session['compare'] = compare
    return redirect(reverse('view_compare'))
