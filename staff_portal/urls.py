from django.urls import path

from .views import (
    staff_orders,
    update_order_status
)

urlpatterns = [

    path(
        'staff/orders/',
        staff_orders,
        name='staff_orders'
    ),

    path(
        'staff/order/<int:order_id>/<str:new_status>/',
        update_order_status,
        name='update_order_status'
    ),
]