from django.shortcuts import render

from orders.models import Order
from django.shortcuts import redirect
from django.http import HttpResponse



def staff_orders(request):
    if request.user.role not in [
    'STAFF',
    'ADMIN'
]:

        return HttpResponse(
            "Access Denied"
    )

    orders = Order.objects.all().order_by(
        '-created_at'
    )

    context = {
        'orders': orders
    }

    return render(
        request,
        'staff_portal/orders.html',
        context
    )
def update_order_status(
    request,
    order_id,
    new_status
):
    if request.user.role not in [
    'STAFF',
    'ADMIN'
]:

        return HttpResponse(
            "Access Denied"
    )

    order = Order.objects.get(
        id=order_id
    )

    order.status = new_status

    order.save()

    return redirect(
        'staff_orders'
    )