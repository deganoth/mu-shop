from django.test import TestCase
from django.shortcuts import get_object_or_404
from products.models import Product, Categorie
from django.contrib.auth.models import User


# Create your tests here.
class TestViews(TestCase):
    def test_get_shopping_cart_page(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
