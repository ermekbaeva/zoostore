from goods.models import Products, Categories
from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

def catalog(request, subcategory_slug):
    page = request.GET.get('page', 1)
    order_by=request.GET.get('order_by', None)

    if subcategory_slug == "all":
        goods = Products.objects.all()
    else:
        goods=get_list_or_404(Products.objects.filter(subcategory__slug=subcategory_slug))

    if order_by and order_by!='default':
        goods=goods.order_by(order_by)
    
    paginator=Paginator(goods, 9)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Catalog',
        'goods': current_page,
        "slug_url": subcategory_slug,
    }
    
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product=Products.objects.get(slug=product_slug)
    context={'product': product}
    return render(request, 'goods/product.html', context=context)