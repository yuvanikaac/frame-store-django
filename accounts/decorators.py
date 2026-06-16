from django.shortcuts import redirect


def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.role != 'ADMIN':
            return redirect('login')

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper


def staff_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.role != 'STAFF':
            return redirect('login')

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper


def customer_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.role != 'CUSTOMER':
            return redirect('login')

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper