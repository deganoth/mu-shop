from django.contrib import admin
from .models import Product, Categorie

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display=('name', 'category', 'description', 'quantity', 'price')
	ordering = ('name',)
	search_fields = ('name', 'category', 'description')

#admin.site.register(Categorie)
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display=('name', 'number')
	ordering = ('name', 'number')
	search_fields = ('name', 'number')