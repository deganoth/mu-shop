from django.db import models


class BannerImage(models.Model):
    name = models.CharField(max_length=254, default='')
    title = models.CharField(max_length=254, default='')
    tag = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
