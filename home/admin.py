from django.contrib import admin
from .models import BannerImage

@admin.register(BannerImage)
class ProductAdmin(admin.ModelAdmin):
	list_display=('name', 'title')
	ordering = ('name', 'title')
	search_fields = ('name', 'title')