from django.shortcuts import render, redirect
from .forms import CustomerSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .decorators import (
    admin_required,
    staff_required,
    customer_required
)


def signup_view(request):

    if request.method == 'POST':

        form = CustomerSignupForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = CustomerSignupForm()

    return render(
        request,
        'accounts/signup.html',
        {'form': form}
    )

from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == 'ADMIN':
                return redirect('admin_dashboard')

            elif user.role == 'STAFF':
                return redirect('staff_dashboard')

            else:
                return redirect('customer_dashboard')

        messages.error(
            request,
            'Invalid email or password'
        )

    return render(
        request,
        'accounts/login.html'
    )

@login_required
@customer_required
def customer_dashboard(request):

    return render(
        request,
        'accounts/customer_dashboard.html'
    )

@login_required
@staff_required
def staff_dashboard(request):

    return render(
        request,
        'accounts/staff_dashboard.html'
    )


@login_required
@admin_required
def admin_dashboard(request):

    return render(
        request,
        'accounts/admin_dashboard.html'
    )

def logout_view(request):

    logout(request)

    return redirect('login')
