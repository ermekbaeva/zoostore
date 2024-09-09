from django.shortcuts import render
from goods.models import Categories, Subcategories, Products
import random

def index(request):
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    discounted_products = Products.objects.filter(discount__gt=0)
    
    discounted_products = random.sample(list(discounted_products), min(len(discounted_products), 12))
    context={
        'title':'Home',
        'content':'Main page',
        'categories':categories,
        'subcategories':subcategories,
        'goods':discounted_products,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context={
        'title':'Home',
        'content':'About page'
    }
    return render(request, 'main/about.html', context)
