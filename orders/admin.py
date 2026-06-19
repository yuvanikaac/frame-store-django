from django.contrib import admin

from .models import (
    Order,
    OrderItem,
    Cart,
    CartItem
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'full_name',
        'phone_number',
        'total_amount',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'full_name',
        'phone_number'
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'customer_upload',
        'quantity',
        'price'
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'created_at'
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        'cart',
        'customer_upload',
        'quantity'
    )