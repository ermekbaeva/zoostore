from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cart_add(request):
    
    if request.method == 'POST':
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)
        else:
            carts = Cart.objects.filter(
                session_key=request.session.session_key, product=product
            )
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
                else:
                    Cart.objects.create(
                        session_key=request.session.session_key, product=product, quantity=1
                    )
        total_items = Cart.objects.filter(user=request.user).total_quantity()
        return JsonResponse({"success": True, "message": "Item was added to cart", "total_items": total_items})

@csrf_exempt
def cart_change(request):
    if request.method == 'POST':
        cart_id = request.POST.get("cart_id")
        quantity = request.POST.get("quantity")
        cart = Cart.objects.get(id=cart_id)
        cart.quantity = quantity
        cart.save()
        response_data = {
                "success": True,
                "message": "Quantity was changed",
                "total_items": Cart.objects.filter(user=request.user).total_quantity(),
                "total_price": Cart.objects.filter(user=request.user).total_price(),
            }
        return JsonResponse(response_data)
    
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=400)

@csrf_exempt
def cart_remove(request):
    print({request.method})
    if request.method == 'POST':
        cart_id = request.POST.get("cart_id")
        cart = Cart.objects.get(id=cart_id)
        quantity = cart.quantity
        cart.delete()
        user_cart = get_user_carts(request)
        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {"carts": user_cart}, request=request
        )
        total_items = Cart.objects.filter(user=request.user).total_quantity()
        response_data = {
            "success": True,
            "message": "Item was removed",
            "cart_items_html": cart_items_html,
            "total_items": total_items,
            "quantity_deleted": quantity,
        }
        return JsonResponse(response_data)
