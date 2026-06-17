from django.contrib import admin

from .models import (
    Frame,
    FrameVariant,
    CustomerUpload
)


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'active',
        'created_at'
    )

    list_filter = (
        'active',
    )

    search_fields = (
        'name',
    )


@admin.register(FrameVariant)
class FrameVariantAdmin(admin.ModelAdmin):

    list_display = (
        'frame',
        'size',
        'orientation',
        'price'
    )

    list_filter = (
        'orientation',
    )

    search_fields = (
        'frame__name',
        'size'
    )
@admin.register(CustomerUpload)
class CustomerUploadAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'frame_variant',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'user__email',
    )