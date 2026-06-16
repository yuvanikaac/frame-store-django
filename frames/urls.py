from django.urls import path

from .views import frame_list

urlpatterns = [

    path(
        'customer/frames/',
        frame_list,
        name='frame_list'
    ),
]