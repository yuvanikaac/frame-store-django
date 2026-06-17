from django.urls import path

from .views import (
    frame_list,
    frame_detail,
    upload_photo
)

urlpatterns = [

    path(
        'customer/frames/',
        frame_list,
        name='frame_list'
    ),

    path(
        'customer/frame/<int:variant_id>/',
        frame_detail,
        name='frame_detail'
    ),
    path(
    'customer/upload-photo/<int:variant_id>/',
    upload_photo,
    name='upload_photo'
),
]