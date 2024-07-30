from goods.models import Products
from django.shortcuts import render
from django.core.paginator import Paginator

from goods.utils import q_search

def catalog(request, subcategory_slug=None):
    page = request.GET.get('page', 1)
    order_by=request.GET.get('order_by', "default")
    min_price = request.GET.get('min_price', 1)
    max_price = request.GET.get('max_price', 500)
    query = request.GET.get('q', None)

    if subcategory_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(subcategory__slug=subcategory_slug)

    if order_by and order_by!='default':
        goods=goods.order_by(order_by)

    if min_price or max_price:
        goods = goods.filter(price__range=(min_price, max_price))
        

    paginator=Paginator(goods, 12)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Catalog',
        'goods': current_page,
        "slug_url": subcategory_slug,
        'min_price': min_price,
        'max_price': max_price,
        'order_by': order_by,
    }
    
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product=Products.objects.get(slug=product_slug)
    context={'product': product}
    return render(request, 'goods/product.html', context=context)