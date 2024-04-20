from django.shortcuts import render
from goods.models import Categories, Subcategories

def index(request):
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()
    context={
        'title':'Home',
        'content':'Main page',
        'categories':categories,
        'subcategories':subcategories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context={
        'title':'Home',
        'content':'About page'
    }
    return render(request, 'main/about.html', context)
