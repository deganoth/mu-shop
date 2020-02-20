from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
	products = Product.objects.all()
	return render(request, "products.html", {'products': products})

def all_guitars(request):
	guitars = Product.objects.filter(category=1)
	return render(request, "guitars.html", {'guitars': guitars})

def all_amps(request):
	amps = Product.objects.filter(category=2)
	return render(request, "amps.html", {'amps': amps})

def all_drums(request):
	drums = Product.objects.filter(category=3)
	return render(request, "drums.html", {'drums': drums})

def all_keys(request):
	keys = Product.objects.filter(category=4)
	return render(request, "keys.html", {'keys': keys})

def all_studio(request):
	studio = Product.objects.filter(category=5)
	return render(request, "studio.html", {'studio': studio})

def view_single(request, id):
	product = Product.objects.filter(id=id)
	return render(request, "single.html", {'id': id, 'product': product})

