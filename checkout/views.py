from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .forms import OrderForm
from.models import Order, OrderLineItem
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

            for product_id, quantity in cart.items():   
                id = request.POST.get('product_id')
                product = get_object_or_404(Product, pk=product_id)

                # IMPORTANT! update product quantities in database
                if quantity:
                    product.quantity -= 1
                    product.save()    

                total = total + quantity * product.price 
                receipt_total = total - quantity * product.price
                
                # converting total to a readable format for stripe. Required for use with MoneyField.
                # the translate method searches through the string for any reference of the selected symbol. 
                # It can replace or remove this symbol.
                x = str(total)
                y = x.translate({ord(i): None for i in '€'})
                z = y.translate({ord(i): None for i in ','})
                new_total = int(float(z))


                order_line_item = OrderLineItem(order=order, product=product, quantity=quantity, sub_total=new_total)
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
                messages.error(request, "Thank you {} for your purchase!".format(order.full_name))
                request.session['cart'] = {}
                return redirect(reverse('checkout_complete'))
            else: 
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card!")
    else:
         order_form = OrderForm()
    
    return render(request, "checkout.html", {'order_form': order_form})

def checkout_complete(request):
    details = OrderLineItem.objects.order_by('order_id')
    emails = User.objects.filter(is_active=True).values_list('email', flat=True)

    subject = 'MuShop purchase'
    html_message = render_to_string('receipt.html', {'details': details})
    plain_message = strip_tags(html_message)
    from_email = 'From <admin@mu-shop.herokuapp.com>'
    to = request.user.email

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    return render(request, 'checkout_complete.html', {'details': details})
