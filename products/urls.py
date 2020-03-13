from django.conf.urls import url, include
from .views import all_products 
from .views import all_guitars
from .views import all_amps
from .views import all_drums
from .views import all_keys
from .views import all_studio
from .views import one_product
from .views import all_reviews
from .views import one_review
from .views import add_review


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<product_id>\d+)/$', one_product, name='single'),
    url(r'^(?P<product_id>\d+)/add_review/$', add_review, name='add_review'),
    url(r'^guitars/', all_guitars, name='guitars'),
    url(r'^amps/', all_amps, name='amps'),
    url(r'^drums/', all_drums, name='drums'),
    url(r'^keys/', all_keys, name='keys'),
    url(r'^studio/', all_studio, name='studio'),
    url(r'^reviews/', all_reviews, name='all_reviews'),
    url(r'^review/(?P<review_id>\d+)/$', one_review, name='one_review'),
    ]
