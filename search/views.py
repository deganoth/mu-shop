from django.shortcuts import render
from products.models import Product
from django.db.models import Q

def do_search(request):
    q = request.GET['results']
    products = Product.objects.filter(
    	Q(name__icontains=q) | 
    	Q(description_line_one__icontains=q) | 
    	Q(description_line_two__icontains=q) |
    	Q(description_line_three__icontains=q) |
    	Q(description_line_four__icontains=q) |
    	Q(short_description__icontains=q)
    	)
    return render(request, "products.html", {'products': products})
