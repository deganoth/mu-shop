from django.shortcuts import render
from .models import BannerImage

# Create your views here.
def all_banners(request):
    banners = BannerImage.objects.all()
    return render(request, "index.html", {'banners': banners})