from django.conf.urls import url, include
from .views import all_products, all_guitars, all_amps, all_drums,  all_keys, all_studio, one_product, all_reviews, one_review, add_review

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<product_id>\d+)/$', one_product, name='single'),
    url(r'^(?P<product_id>\d+)/add_review/$', add_review, name='add_review'),
    url(r'^categories/', all_guitars, name='guitars'),
    url(r'^guitars/', all_guitars, name='guitars'),
    url(r'^amps/', all_amps, name='amps'),
    url(r'^drums/', all_drums, name='drums'),
    url(r'^keys/', all_keys, name='keys'),
    url(r'^studio/', all_studio, name='studio'),
    url(r'^reviews/', all_reviews, name='all_reviews'),
    url(r'^review/(?P<review_id>\d+)/$', one_review, name='one_review'),
    ]   