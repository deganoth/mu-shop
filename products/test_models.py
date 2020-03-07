from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Categorie, Review

# Create your tests here.

class TestCategorieModel(TestCase):
	def test_category_name_as_a_string(self):
		category = Categorie()
		category.name="Create a Name"
		self.assertEqual("Create a Name", str(category)) 

	def test_review_name_as_a_string(self):
		review = Review()
		review.comment="Create a Name"
		self.assertEqual("Create a Name", str(review)) 