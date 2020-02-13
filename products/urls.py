from django.conf.urls import url, include
from .views import all_products, all_guitars, all_keys

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^guitars/', all_guitars, name='guitars'),
    url(r'^keys/', all_keys, name='keys'),
    ]