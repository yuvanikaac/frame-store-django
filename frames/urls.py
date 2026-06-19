

from django.urls import path

from .views import (
    frame_list,
    frame_detail,
    upload_photo,
    preview_frame,
    wall_preview,
    save_preview
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
    path(
    'customer/preview/<int:upload_id>/',
    preview_frame,
    name='preview_frame'
    ),

     path(
        'customer/wall-preview/<int:upload_id>/',
        wall_preview,
        name='wall_preview'
        ),
        path(
        'customer/save-preview/<int:upload_id>/',
        save_preview,
        name='save_preview'
        ),


   

   
]

