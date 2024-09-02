from django.http import JsonResponse
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cart_add(request):
    if request.method == "POST":
        try:
            product_id = request.POST.get("product_id")
            product = Products.objects.get(id=product_id)
            if request.user.is_authenticated:
                user_identifier = request.user
                carts = Cart.objects.filter(user=user_identifier, product=product)
            else:
                if not request.session.session_key:
                    request.session.create()
                session_key = request.session.session_key
                user_identifier = session_key
                carts = Cart.objects.filter(session_key=session_key, product=product)

            if carts.exists():
                cart = carts.first()
                cart.quantity += 1
                cart.save()
            else:
                Cart.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    session_key=session_key if not request.user.is_authenticated else None,
                    product=product,
                    quantity=1
                )
            total_items = get_user_carts(request).total_quantity()
            return JsonResponse(
                {
                    "success": True,
                    "message": "Item was added to cart",
                    "total_items": total_items,
                }
            )
        except Products.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
def cart_change(request):
    if request.method == "POST":
        try:
            cart_id = request.POST.get("cart_id")
            quantity = request.POST.get("quantity")
            cart = Cart.objects.get(id=cart_id)
            cart.quantity = quantity
            cart.save()
            total_items = get_user_carts(request).total_quantity()
            total_price = get_user_carts(request).total_price()
            products_price = cart.products_price()
            response_data = {
                "success": True,
                "message": "Quantity was changed",
                "total_items": total_items,
                "total_price": total_price,
                "products_price": products_price,
            }
            return JsonResponse(response_data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
def cart_remove(request):
    if request.method == "POST":
        try:
            cart_id = request.POST.get("cart_id")
            cart = Cart.objects.get(id=cart_id)
            quantity = cart.quantity
            cart.delete()
            total_items = get_user_carts(request).total_quantity()
            total_price = get_user_carts(request).total_price()
            response_data = {
                "success": True,
                "message": "Item was removed",
                "total_items": total_items,
                "total_price": total_price,
                "quantity_deleted": quantity,
            }
            return JsonResponse(response_data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
