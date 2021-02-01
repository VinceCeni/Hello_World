from django.shortcuts import render
from django.http import HttpResponse
from .models import products

def admin_console(request):
    Product = Product.objects.all()
    return render(request, 'products/product_page.html', {'products': products})

# Create your views here.
