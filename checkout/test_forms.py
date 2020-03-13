from django.test import TestCase
from .forms import OrderForm
# Create your tests here.


class TestToDoOrderForm(TestCase):
    def test_can_create_an_review_with_rating_and_comment(self):
        form = OrderForm(
            {
                'full_name': 'a name',
                'phone_number': 'a number',
                'country': 'a country',
                'postcode': 'a postcode',
                'town_or_city': 'a city',
                'street_address1': 'address one',
                'street_address2': 'address two',
                'county': 'a county'
            }
        )
        self.assertTrue(form.is_valid())
