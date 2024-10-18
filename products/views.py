from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from django.shortcuts import redirect
from .models import Product


# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('Welcome to PyShop New Arrivals')

# views.py


def add_to_cart(request, product_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1  # Increment quantity
        request.session['cart'] = cart
        return JsonResponse({'success': True, 'message': 'Product added to cart'})
    else:
        return redirect('index')  # Redirect to index if not an AJAX request

    
def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product.price * quantity
            })
        except Product.DoesNotExist:
            pass

    # Calculate the total amount for the cart
    total_amount = sum(item['total_price'] for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_amount': total_amount
    })
