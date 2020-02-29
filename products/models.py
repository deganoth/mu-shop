from djmoney.models.fields import MoneyField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import numpy as np

class Categorie(models.Model):
	name = models.CharField(max_length=254, default='')
	description = models.TextField()
	
	def __str__(self):
		return self.name
		
class Product(models.Model):
	name = models.CharField(max_length=254, default='')
	name_overflow = models.CharField(max_length=254, default='')
	category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	short_description = models.CharField(max_length=254, default='')
	description_line_one = models.CharField(max_length=254, default='')
	description_line_two = models.CharField(max_length=254, default='')
	description_line_three = models.CharField(max_length=254, default='')
	description_line_four = models.CharField(max_length=254, default='')
	price = MoneyField(max_digits=6, decimal_places=2, default_currency='EUR')
	quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	image_one = models.ImageField(upload_to='images')
	image_two = models.ImageField(upload_to='images')
	image_three = models.ImageField(upload_to='images')
	image_four = models.ImageField(upload_to='images')

	def average_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(list(all_ratings))

	def __str__(self):
		return self.name

class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', null=True)	
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(6),MinValueValidator(1)])

    def __str__(self):
    	return self.comment