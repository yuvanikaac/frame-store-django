from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Cart,
    CartItem,
    Order,
    OrderItem
)


class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0

    readonly_fields = (
        'photo_preview',
        'frame_name',
        'frame_size',
        'frame_orientation',
        'frame_thickness'
    )

    fields = (
        'photo_preview',
        'frame_name',
        'frame_size',
        'frame_orientation',
        'frame_thickness',
        'quantity',
        'price'
    )

    def photo_preview(self, obj):

        if (
            obj.customer_upload
            and
            obj.customer_upload.photo
    ):

            return format_html(

                '<a href="{}" target="_blank">'
                '<img src="{}" width="120"/>'
                '</a>',

                obj.customer_upload.photo.url,

                obj.customer_upload.photo.url
            )

        return "-"

    def frame_name(self, obj):

        return (
            obj.customer_upload
            .frame_variant
            .frame
            .name
        )

    def frame_size(self, obj):

        return (
            obj.customer_upload
            .frame_variant
            .size
        )

    def frame_orientation(self, obj):

        return (
            obj.customer_upload
            .frame_variant
            .orientation
        )

    def frame_thickness(self, obj):

        return (
            obj.customer_upload
            .frame_variant
            .thickness
        )

    photo_preview.short_description = (
        "Customer Photo"
    )

    frame_name.short_description = (
        "Frame"
    )

    frame_size.short_description = (
        "Size"
    )

    frame_orientation.short_description = (
        "Orientation"
    )

    frame_thickness.short_description = (
        "Thickness"
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

    inlines = [
        OrderItemInline
    ]


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