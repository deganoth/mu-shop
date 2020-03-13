from django.conf.urls import url
from .views import view_compare, add_to_compare, delete_compare

urlpatterns = [
    url(r'^$', view_compare, name='view_compare'),
    url(r'^add/(?P<id>\d+)', add_to_compare, name='add_to_compare'),
    url(r'^adjust/(?P<id>\d+)', delete_compare, name='delete_compare'),
    ]
