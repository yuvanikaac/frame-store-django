from django.shortcuts import (
    redirect,
    render
)

from .models import (
    Cart,
    CartItem,
    Order,
    OrderItem
)
#from django.shortcuts import render
#from .models import Order

from frames.models import (
    CustomerUpload
)


def add_to_cart(request, upload_id):

    upload = CustomerUpload.objects.get(
        id=upload_id
    )

    cart, created = Cart.objects.get_or_create(

        user=request.user
    )

    CartItem.objects.create(

        cart=cart,

        customer_upload=upload,

        quantity=1
    )

    return redirect(
        'cart_detail'
    )
def cart_detail(request):

    cart = Cart.objects.get(
        user=request.user
    )

    total = 0

    for item in cart.items.all():

        total += item.total_price

    context = {

        'cart': cart,

        'total': total
    }

    return render(
        request,
        'orders/cart.html',
        context
    )
def remove_cart_item(request, item_id):

    item = CartItem.objects.get(
        id=item_id
    )

    item.delete()

    return redirect(
        'cart_detail'
    )

def checkout(request):

    cart = Cart.objects.get(
        user=request.user
    )

    total = 0

    for item in cart.items.all():

        total += item.total_price

    if request.method == 'POST':

        order = Order.objects.create(

            user=request.user,

            full_name=request.POST.get(
                'full_name'
            ),

            phone_number=request.POST.get(
                'phone_number'
            ),

            address_line_1=request.POST.get(
                'address_line_1'
            ),

            address_line_2=request.POST.get(
                'address_line_2'
            ),

            city=request.POST.get(
                'city'
            ),

            state=request.POST.get(
                'state'
            ),

            pincode=request.POST.get(
                'pincode'
            ),

            total_amount=total
        )

        for item in cart.items.all():

            OrderItem.objects.create(

                order=order,

                customer_upload=
                item.customer_upload,

                quantity=item.quantity,

                price=
                item.customer_upload
                .frame_variant
                .price
            )

        cart.items.all().delete()

        return redirect(
            'order_success'
        )

    context = {

        'cart': cart,

        'total': total
    }

    return render(
        request,
        'orders/checkout.html',
        context
    )
def order_success(request):

    return render(
        request,
        'orders/order_success.html'
    )