from django.conf.urls import url, include
from .views import all_products, all_guitars, all_amps, all_drums,  all_keys, all_studio

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^guitars/', all_guitars, name='guitars'),
    url(r'^amps/', all_amps, name='amps'),
    url(r'^drums/', all_drums, name='drums'),
    url(r'^keys/', all_keys, name='keys'),
    url(r'^studio/', all_studio, name='studio'),
    ]