from django.shortcuts import render

from .models import FrameVariant
from .models import CustomerUpload


def frame_list(request):

    sizes = FrameVariant.objects.values_list(
        'size',
        flat=True
    ).distinct()

    selected_size = request.GET.get('size')

    selected_orientation = request.GET.get(
        'orientation'
    )

    frame_variants = FrameVariant.objects.all()

    if selected_size:

        frame_variants = frame_variants.filter(
            size=selected_size
        )

    if selected_orientation:

        frame_variants = frame_variants.filter(
            orientation=selected_orientation
        )

    context = {

        'frame_variants': frame_variants,

        'sizes': sizes,

        'selected_size': selected_size,

        'selected_orientation': selected_orientation,
    }

    return render(
        request,
        'frames/frame_list.html',
        context
    )

def frame_detail(request, variant_id):

    variant = FrameVariant.objects.get(
        id=variant_id
    )

    context = {
        'variant': variant
    }

    return render(
        request,
        'frames/frame_detail.html',
        context
    )
def upload_photo(request, variant_id):

    variant = FrameVariant.objects.get(
        id=variant_id
    )

    if request.method == 'POST':

        photo = request.FILES.get(
            'photo'
        )

        if photo:

            CustomerUpload.objects.create(

                user=request.user,

                frame_variant=variant,

                photo=photo,

                status='TEMP'
            )

            return render(
                request,
                'frames/upload_success.html'
            )

    context = {
        'variant': variant
    }

    return render(
        request,
        'frames/upload_photo.html',
        context
    )