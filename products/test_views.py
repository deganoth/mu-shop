from django.test import TestCase
from django.shortcuts import get_object_or_404
from models import Product, Categorie, Review
from forms import ReviewForm
from django.contrib.auth.models import User


# Create your tests here.

class TestViews(TestCase):

    def test_get_products_page(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')

        def test_get_guitars_category(self):
            page = self.client.get('/products/guitars/')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'guitars.html')

        def test_get_amps_category(self):
            page = self.client.get('/products/amps/')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'amps.html')

        def test_get_drums_category(self):
            page = self.client.get('/products/drums/')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'drums.html')

        def test_get_keys_category(self):
            page = self.client.get('/products/keys/')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'keys.html')

        def test_get_studio_category(self):
            page = self.client.get('/products/studio/')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'studio.html')

        def test_get_one_product_page(self):
            category = Categorie(name='A name')
            category.save()
            product = Product(id=4, name='Create a Name',
                              category=category, price=12)
            product.save()
            page = self.client.get('/products/{0}/'.format(product.id))
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'single.html')

        def test_get_reviews_page(self):
            page = self.client.get('/products/reviews/')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'all_reviews.html')

        def test_get_one_review_page(self):
            review = Review(id=2)
            page = \
                self.client.get('/products/review/{0}/'.format(review.id))
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'one_review.html')

        def test_create_review(self):
            review = Review(id=1)
            response = self.client.post('/products/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'products.html')

        def test_add_admin_form_view(self):
            review_count = Review()
            response = self.client.post(
                '/products/', {
                    'rating': 5, 'comment': 'a comment'
                    }
                    )
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content)
