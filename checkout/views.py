from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm
from.models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import os
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price

                # converting total to a readable format for stripe. Required for use with MoneyField.
                # the translate method searches through the string for any reference of the selected symbol. 
                # It can replace or remove this symbol.
                x = str(total)
                y = x.translate({ord(i): None for i in '€'})
                z = y.translate({ord(i): None for i in ','})
                new_total = int(float(z))
              
                order_line_item = OrderLineItem(order=order, product=product, quantity=quantity)
                order_line_item.save()
            
            try: 
                # IMPORTANT! card must be declared as a reference to the stripe_id retrieved from the checkout form.
                
                card = request.POST.get('stripe_id')
                customer = stripe.Charge.create(
                    amount = new_total * 100,
                    currency = 'eur',
                    description = request.user.email,
                    card = card,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else: 
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card!")
    else:
         order_form = OrderForm()
 
    return render(request, "checkout.html", {'order_form': order_form})
