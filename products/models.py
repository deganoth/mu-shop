from djmoney.models.fields import MoneyField
from django.db import models

class Categorie(models.Model):
	name = models.CharField(max_length=254, default='')
	number = models.CharField(max_length=254, default='')
	description = models.TextField()
	
	def __str__(self):
		return self.name
		
class Product(models.Model):
	name = models.CharField(max_length=254, default='')
	category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	description = models.TextField()
	price = MoneyField(max_digits=6, decimal_places=2, default_currency=None)
	quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	image = models.ImageField(upload_to='images')
	
	def __str__(self):
		return self.name