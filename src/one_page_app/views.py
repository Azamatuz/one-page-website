from django.shortcuts import render
from .models import CarouselSlide, Product

def home(request):
    carousel_slides = CarouselSlide.objects.all()
    products = Product.objects.all()

    return render(request, 'home.html', {'carousel_slides': carousel_slides, 'products': products})
