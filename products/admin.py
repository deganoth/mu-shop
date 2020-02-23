from django.contrib import admin
from .models import Product, Categorie, Review

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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ('pub_date', 'user_name')
    search_fields = ('comment', )
    

