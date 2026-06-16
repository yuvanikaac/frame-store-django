from django.urls import path

from .views import (
    signup_view,
    login_view,
    customer_dashboard,
    staff_dashboard,
    admin_dashboard,
    logout_view
)

urlpatterns = [

    path(
        'signup/',
        signup_view,
        name='signup'
    ),

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'customer-dashboard/',
        customer_dashboard,
        name='customer_dashboard'
    ),

    path(
        'staff-dashboard/',
        staff_dashboard,
        name='staff_dashboard'
    ),

    path(
        'admin-dashboard/',
        admin_dashboard,
        name='admin_dashboard'
    ),

    path(
    'logout/',
    logout_view,
    name='logout'
    ),
]