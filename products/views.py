from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Review
from .forms import ReviewForm
import datetime	

# Create your views here.
def all_products(request):
	product = Product.objects.order_by('name')
	paginator = Paginator(product, 5)

	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, "products.html", {'products': products})

def all_guitars(request):
	guitars = Product.objects.filter(category_id=7)
	return render(request, "guitars.html", {'guitars': guitars})

def all_amps(request):
	amps = Product.objects.filter(category=8)
	return render(request, "amps.html", {'amps': amps})

def all_drums(request):
	drums = Product.objects.filter(category=9)
	return render(request, "drums.html", {'drums': drums})

def all_keys(request):
	keys = Product.objects.filter(category=10)
	return render(request, "keys.html", {'keys': keys})

def all_studio(request):
	studio = Product.objects.filter(category=11)
	return render(request, "studio.html", {'studio': studio})

def one_product(request, product_id):
	product = Product.objects.filter(pk=product_id)
	form = ReviewForm()
	return render(request, "single.html", {'product': product, 'form': form})

def all_reviews(request):
    latest_reviews = Review.objects.order_by('pub_date')
    return render(request, 'all_reviews.html', {'latest_reviews': latest_reviews})

def one_review(request, review_id):
    review = Review.objects.filter(pk=review_id)
    return render(request, 'one_review.html', {'review': review})

@login_required()
def add_review(request, product_id):
	if request.method == "POST":
		product = get_object_or_404(Product, pk=product_id)
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			rating = form.cleaned_data['rating']
			comment = form.cleaned_data['comment']
			user_name = request.user
			review = Review()
			review.product = product
			review.user_name = user_name
			review.rating = rating
			review.comment = comment
			review.pub_date = datetime.datetime.now()
			review.save()

			messages.success(request, "Thank you {0} for your {1} review!".format(user_name, product))
	else:
		form = ReviewForm()

	return redirect(reverse('products'))

