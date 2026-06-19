from django.urls import path

from .views import (
    add_to_cart,
    cart_detail,
    remove_cart_item,
    checkout,
    order_success
)

urlpatterns = [

    path(
        'customer/add-to-cart/<int:upload_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'customer/cart/',
        cart_detail,
        name='cart_detail'
    ),

    path(
        'customer/remove-cart-item/<int:item_id>/',
        remove_cart_item,
        name='remove_cart_item'
    ),

    path(
        'customer/checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'customer/order-success/',
        order_success,
        name='order_success'
    ),

]