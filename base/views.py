from django.shortcuts import render
from django.http import Http404

from .models import Category, Meat

def base(request):
    return render(request, 'main/index.html')

def log_in(request):
    return render(request, 'account/log_in.html')

def product(request):
    return render(request, 'product/product.html')

def about(request):
    return render(request, 'main/about-us.html')

