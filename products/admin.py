from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display=('name', 'category', 'description')
	ordering = ('name',)
	search_fields = ('name', 'category', 'description')

#admin.site.register(Product)