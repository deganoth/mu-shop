from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product, Categorie
# Create your tests here.


class TestOrderModel(TestCase):
    def test_order_has_string_output(self):
        order = Order()
        order.full_name = "Create a Name"
        order.id = " An Id"
        order.date = "A Date"
        result = " {0}-{1}-{2}".format(order.id, order.date, order.full_name)
        self.assertEqual("An Id-A Date-Create a Name", str(result))

    def test_order_line_item_has_output(self):
        category = Categorie(name="A name")
        category.save()
        product = Product(
            name="Create a Name",
            category=category,
            price=12
            )
        product.save()
        order = Order(
            id="An Id",
            full_name="Create a Name",
            phone_number="Create a Number",
            country="Create a Country",
            town_or_city="Create a Town",
            street_address1="Create an address",
            street_address2="Create an address",
            county="Create a County"
            )
        order_line = OrderLineItem(product=product, order=order, quantity=2)
        result = "{0} {1} @ {2} {3}".format(
            order_line.order.id, order_line.quantity, order_line.product.name, order_line.product.price
            )
        self.assertEqual("An Id 2 @ Create a Name 12.00 €", str(result))
        self.assertTrue(order_line.total())
