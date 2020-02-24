from django.conf.urls import url, include
from .views import all_banners

urlpatterns = [
	url(r'^$', all_banners, name='all_banners'),
]
