from django.contrib import admin

from .models import Frame, FrameVariant


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