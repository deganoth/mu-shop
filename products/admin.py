from django.contrib import admin
from .models import Product, Categorie, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'short_description', 'quantity', 'price'
        )
    ordering = ('name', )
    search_fields = ('name', 'category', 'short_description')


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )
    search_fields = ('name', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'rating', 'user_name', 'comment', 'pub_date'
        )
    list_filter = ('pub_date', 'user_name')
    search_fields = ('comment', )
