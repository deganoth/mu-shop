from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
	products = Product.objects.all()
	return render(request, "products.html", {'products': products})

def all_guitars(request):
	guitars = Product.objects.filter(category='Guitars')
	return render(request, "guitars.html", {'guitars': guitars})

def all_keys(request):
	keys = Product.objects.filter(category='Keys')
	return render(request, "keys.html", {'keys': keys})


