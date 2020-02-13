from django.db import models

class BannerImage(models.Model):
	name = models.CharField(max_length=254, default='')
	image = models.ImageField(upload_to='images')
	
	def __str__(self):
		return self.name
		