from django.test import TestCase
from .forms import ReviewForm
# Create your tests here.
class TestToDoReviewForm(TestCase):
	def test_can_create_an_review_with_rating_and_comment(self):
		form  = ReviewForm(
			{'rating': 5, 
			'comment': 'a comment'
			}
			)
		self.assertTrue(form.is_valid())
