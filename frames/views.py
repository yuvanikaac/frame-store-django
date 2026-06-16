from django.shortcuts import render

from .models import FrameVariant


def frame_list(request):

    size = request.GET.get('size')

    orientation = request.GET.get('orientation')

    frame_variants = FrameVariant.objects.all()

    if size:

        frame_variants = frame_variants.filter(
            size=size
        )

    if orientation:

        frame_variants = frame_variants.filter(
            orientation=orientation
        )

    context = {

        'frame_variants': frame_variants,

        'selected_size': size,

        'selected_orientation': orientation,
    }

    return render(
        request,
        'frames/frame_list.html',
        context
    )