from django.urls import path
from .views import index, new, add_to_cart, cart

urlpatterns = [
    path('', index, name='index'),
    path('new/', new, name='new'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/', cart, name='cart'),
]
